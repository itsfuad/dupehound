# DupeHound

Find redundant copies of files before archiving disks. Read-only: this tool
never removes, moves or modifies the files it scans.

Designed for Python 2.7 and Python 3, with no third-party dependencies.

## Usage

```
python cli.py ~/Downloads ~/old-backup
python cli.py --json ~/Downloads > duplicates.json
python -m unittest discover -s tests
```

Hashing runs only for files that share a size, so most unique files are cheap
to rule out. Compare the paths manually before deleting anything.

`--summary` reports possible savings if you keep one copy of each identical
content group. It does not account for filesystem hard links or compression.
