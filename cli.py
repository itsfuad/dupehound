from __future__ import print_function
import argparse
import json
from dupehound import duplicates


def main(argv=None):
    parser = argparse.ArgumentParser(description='Read-only duplicate file report')
    parser.add_argument('roots', nargs='+', help='Directories or individual files')
    parser.add_argument('--json', action='store_true', help='Machine-readable results')
    args = parser.parse_args(argv)
    results = duplicates(args.roots)
    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
    else:
        if not results:
            print('No duplicate groups found.')
        for group in results:
            print('%d bytes, %d copies:' % (group['size'], len(group['files'])))
            for path in group['files']:
                print('  ' + path)
    return 0


if __name__ == '__main__':
    main()
