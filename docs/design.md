# Why compare content, not file names?

Backups often rename files and cameras reuse the same names. Equal file size
is only a candidate: we compute SHA-256 on those candidates before reporting.

Symlinks are skipped because following them can scan the same directory
multiple times or leave the selected root. The command is deliberately read-only.
