from __future__ import print_function
import os
import hashlib


def walk_files(roots):
    """Yield normal files; skip symbolic links and unreadable directories."""
    for root in roots:
        if os.path.isfile(root) and not os.path.islink(root):
            yield root
            continue
        for dirname, dirs, files in os.walk(root, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not os.path.islink(os.path.join(dirname, d)))
            for name in sorted(files):
                path = os.path.join(dirname, name)
                if os.path.isfile(path) and not os.path.islink(path):
                    yield path


def checksum(path, chunk_size=65536):
    h = hashlib.sha256()
    with open(path, 'rb') as stream:
        while True:
            block = stream.read(chunk_size)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def duplicates(roots):
    sizes = {}
    seen = set()
    for path in walk_files(roots):
        canonical = os.path.abspath(path)
        if canonical in seen:
            continue
        seen.add(canonical)
        try:
            size = os.stat(path).st_size
        except (IOError, OSError):
            continue
        sizes.setdefault(size, []).append(path)
    result = []
    for size, paths in sorted(sizes.items()):
        if len(paths) < 2:
            continue
        by_hash = {}
        for path in paths:
            try:
                digest = checksum(path)
            except (IOError, OSError):
                continue
            by_hash.setdefault(digest, []).append(path)
        for digest, matches in sorted(by_hash.items()):
            if len(matches) > 1:
                result.append({'size': size, 'sha256': digest, 'files': sorted(matches)})
    return result
