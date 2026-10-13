"""Read V3 metadata or scoped rows without traversing parent/reference links."""
import argparse
import hashlib
import json
import re
from pathlib import Path

DEFAULT_DICTIONARY = Path(__file__).resolve().parents[1] / 'references/game-domain-dictionary-v3.md'
COLUMNS = ('key', 'value', '구별 기준', '보고서 예문', '의미 차이', 'ref')


def read_dictionary(path):
    raw = path.read_bytes()
    document = raw.decode('utf-8')
    header = re.match(r'\A<!-- game-domain-metadata\s*\n(.*?)\n-->\s*\n', document, re.S)
    if not header:
        raise ValueError('Missing leading game-domain-metadata JSON comment')
    metadata = json.loads(header[1])
    if metadata.get('schema') != 'game-domain-dictionary-query/1':
        raise ValueError('Unsupported dictionary schema')
    nodes = metadata.get('nodes')
    if not isinstance(nodes, dict) or not nodes:
        raise ValueError('Missing dictionary nodes')

    body = document[header.end():]
    positions = {}
    for node_id, node in nodes.items():
        if not isinstance(node, dict) or not isinstance(node.get('anchor'), str):
            raise ValueError(f'Invalid node: {node_id}')
        for field in ('genre_name_keys', 'references'):
            values = node.get(field, [])
            if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                raise ValueError(f'{field} must be a string array: {node_id}')
        matches = list(re.finditer(rf'^<a id="{re.escape(node["anchor"])}"></a>$', body, re.M))
        if len(matches) != 1:
            raise ValueError(f'Missing or duplicate registered anchor: {node_id}')
        positions[node_id] = matches[0].start()
        if 'parent' not in node or (node['parent'] is not None and node['parent'] not in nodes):
            raise ValueError(f'Invalid parent: {node_id}')
        if any(ref not in nodes for ref in node.get('references', [])):
            raise ValueError(f'Invalid reference: {node_id}')
    if len(set(positions.values())) != len(nodes):
        raise ValueError('Registered nodes share an anchor')
    for node_id in nodes:
        chain = set()
        current = node_id
        while current is not None:
            if current in chain:
                raise ValueError(f'Parent cycle: {node_id}')
            chain.add(current)
            current = nodes[current]['parent']
    return metadata, body, positions, hashlib.sha256(raw).hexdigest()


def query_rows(metadata, body, positions, node_ids, mode='all', scope='subtree', keys=()):
    nodes = metadata['nodes']
    for node_id in node_ids:
        if node_id not in nodes:
            raise ValueError(f'Unknown node ID: {node_id}')
    selected = set(node_ids)
    if scope == 'subtree':
        pending = list(selected)
        while pending:
            current = pending.pop()
            for child, node in nodes.items():
                if node['parent'] == current and child not in selected:
                    selected.add(child)
                    pending.append(child)

    rows = []
    ordered = sorted(nodes, key=positions.get)
    for index, node_id in enumerate(ordered):
        if node_id not in selected:
            continue
        end = positions[ordered[index + 1]] if index + 1 < len(ordered) else len(body)
        section = body[positions[node_id]:end]
        names = set(nodes[node_id].get('genre_name_keys', []))
        # ponytail: V3 has six-column tables; escaped pipes are supported. A new
        # table schema should update this parser, rather than adding Markdown dependencies.
        for line in section.splitlines():
            if not line.startswith('|'):
                continue
            cells = [cell.strip() for cell in re.split(r'(?<!\\)\|', line.strip()[1:-1])]
            if cells[0] == 'key' or all(re.fullmatch(r':?-+:?', cell) for cell in cells):
                continue
            if len(cells) != len(COLUMNS):
                raise ValueError(f'Invalid six-column table row: {node_id}')
            is_name = cells[0] in names
            if mode == 'genre_names' and not is_name:
                continue
            if mode == 'terms' and is_name:
                continue
            if keys and cells[0] not in keys:
                continue
            rows.append({'node_id': node_id, **dict(zip(COLUMNS, cells))})
    missing = set(keys) - {row['key'] for row in rows}
    if missing:
        raise ValueError(f'Keys absent from selected scope/mode: {sorted(missing)}')
    return rows, {node_id: nodes[node_id] for node_id in ordered if node_id in selected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('node_ids', nargs='*', help='Exact registered IDs; references require a separate invocation')
    parser.add_argument('--dictionary', type=Path, default=DEFAULT_DICTIONARY)
    parser.add_argument('--list', action='store_true', help='Only metadata, no body rows')
    parser.add_argument('--mode', choices=('all', 'genre_names', 'terms'), default='all')
    parser.add_argument('--scope', choices=('subtree', 'direct'), default='subtree')
    parser.add_argument('--key', action='append', default=[], help='Exact key filter within selected rows; repeatable')
    args = parser.parse_args()
    if args.list and (args.node_ids or args.key):
        parser.error('--list does not accept node IDs or keys')
    if not args.list and not args.node_ids:
        parser.error('Select registered node IDs or use --list first')
    try:
        metadata, body, positions, digest = read_dictionary(args.dictionary)
        result = {'dictionary': str(args.dictionary.resolve()), 'sha256': digest, 'schema': metadata['schema']}
        if args.list:
            result.update(query=metadata.get('query'), nodes=metadata['nodes'])
        else:
            rows, selected = query_rows(metadata, body, positions, args.node_ids, args.mode, args.scope, args.key)
            result.update(selected_node_ids=args.node_ids, mode=args.mode, scope=args.scope, nodes=selected, rows=rows)
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, AttributeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
