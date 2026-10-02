# CLAUDE.md — PYGuide

Coding rules: follow the existing verified examples and the verification environment in README.md; no separate rules file is planned.

## Purpose and scope
- Personal Python reference cookbook: one topic per file, a flat list of
  independent snippets with the result written inline. Not a tutorial or
  an application: add no entry point, CLI, test suite or CI.
- Python 3.10+, the standard library and the libraries in
  `requirements.txt` (unpinned). A new third-party import goes into
  `requirements.txt` and the README "Requirements" table.
- The machine-learning files are syntax references, not modelling advice;
  where the shortcut shown would leak test data, say so in a `# Note:`.
- The default branch is `main`.

## Structure
- Topic files are `PascalCase.py` in the repository root (`ErrorHandling.py`,
  `NumPy.py`, `SQL.py`). Fixtures live in `data/` (small synthetic files
  only); otherwise use seaborn's built-in datasets. `serhatmodule/` exists
  only to back `Module.py`.
- Sections inside a file: `# === Section ===`, optionally numbered
  (`# === 1. Model Selection ===`).
- A new file gets a row in its README "Topic Index" table
  (`` `File.py` `` | what it covers | lines); keep the Lines column and the
  "Requirements" and "Data Files" lists current when a file changes.
- Files that write artifacts (`database.db`, `test.txt`, plots) list them
  in README "Getting Started" and `.gitignore`.

## Code examples
- 4-space indentation, snake_case names; keep each file's quote style.
- Each snippet starts with a sentence-case comment saying what it does.
- Single-line result: `expr # Output: <value>` in the interpreter's repr.
  Multi-line result: `# Output:` on its own line, then one `# ` line per
  output line, exactly as printed.
- Plotting calls carry `# Renders: <what is drawn>` instead of `# Output:`.
- Every example that prints output carries verified `# Output:` comments.
  Never write an output that was not produced by running the code; if it
  cannot be run, say so instead of writing the comment.
- A changed example is re-run in the environment named in README
  "Verified Environment" before its output comments are updated. Run whole
  files from the repository root, top to bottom: earlier snippets change
  the state later outputs depend on.
- A result that depends on the library version gets
  `# Behaviour varies by version: <what differs and from which version>`
  under the output, never one version's output presented as universal.
- Non-deterministic results are shown as `# Output: varies, e.g. <value>`;
  `input()` examples show a `# Sample session:` block instead.

## Links
- Files in README tables are backticked names, not links; links are
  relative (`[LICENSE](LICENSE)`) or in-page anchors
  (`[Verified Environment](#verified-environment)`).
- Code comments name files by repo-root path (`data/employees.csv`).
- External links: github.com/serhatmercan only.
