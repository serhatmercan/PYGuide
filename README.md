# PYGuide — Personal Python Notes & Practical Reference

## Overview

This is a personal reference cookbook of Python snippets — my own notes, kept as short, runnable-in-your-head examples with the expected result written inline as a comment. It is **not** a tutorial and **not** an application; there's no entry point, no CLI, and the files aren't meant to be run top to bottom. Each file covers one topic as a flat list of independent snippets.

## How to Use

- Open the file for the topic you want (see the index below) and read top to bottom.
- Every snippet shows its result as a `# Output:` comment — you can read the answer without running anything.
- To find how a specific method or function is used, search for it by name across files (`grep`, your editor's project search, etc.) — that's the intended way to navigate this repo, not a table of contents.
- A few files load small fixture files from `data/`, or seaborn's built-in datasets (`tips`, `titanic`) — see **Data Files** below.

## Topic Index

Each row's description is drawn from what the file actually contains, not from its name. Line counts as of this review.

### Language Basics

| File | Covers | Lines |
|---|---|---|
| `Boolean.py` | Defining a boolean and checking its type | 4 |
| `Input.py` | Reading user input with `input()` and building a greeting from it (sample session shown, since the real output depends on what you type) | 11 |
| `Conditionals.py` | Comparison/logical operators, `if`/`elif`/`else`, and membership tests (`in`/`not in`) across dict, list, set, and tuple | 37 |
| `Conversion.py` | Converting between `str`, `int`, and `float` | 7 |
| `Loops.py` | `break`/`continue`, `for` loops over lists, dicts, sets, tuples, and DataFrame columns, and `while` loops | 82 |
| `Numbers.py` | `type()` on `float` and `int` | 5 |
| `Strings.py` | Indexing, slicing, and common string methods (`capitalize`, `count`, `split`, `upper`) | 44 |

### Data Structures

| File | Covers | Lines |
|---|---|---|
| `Dictionary.py` | Creating dictionaries, accessing keys/values, `.get()` with a default, adding entries | 25 |
| `List.py` | Indexing, slicing, comprehensions, and common list methods (`append`, `insert`, `pop`, `sort`, `reverse`) | 60 |
| `Set.py` | Creating sets, union, intersection, and converting a list to a set to drop duplicates | 24 |
| `Tuple.py` | Creating tuples, indexing, `count()`, and `index()` on an immutable sequence | 16 |

### Functions & Structure

| File | Covers | Lines |
|---|---|---|
| `Annotation.py` | Variable, function, class, and list type annotations, including the modern `list[int]` generic and `int \| str` union syntax | 48 |
| `Functions.py` | Default arguments, `*args`/`**kwargs`, `enumerate`, `filter`, `lambda`, `map`, `random`, `range`, `zip` | 96 |
| `Module.py` | Importing a module, a name from it, and a submodule three different ways, backed by a small local stub package (`serhatmodule/`) so the example actually runs | 24 |
| `OOP.py` | Classes, inheritance, encapsulation, polymorphism, and abstraction via `abc.ABC` | 108 |
| `ErrorHandling.py` | `try`/`except`, `else`, `finally`, `raise`, and custom exceptions | 52 |
| `Files.py` | Writing, reading, and appending to a local text file | 19 |

### Data Analysis

| File | Covers | Lines |
|---|---|---|
| `NumPy.py` | Array creation, indexing/slicing, arithmetic, matrix operations, random arrays, linear algebra | 127 |
| `Pandas.py` | Series and DataFrame creation, `.loc`/`.iloc`, Excel/CSV I/O, missing-data handling, `groupby`, `concat`/`merge`, `.apply()` — the deepest file in the repo | 648 |
| `DateTime.py` | Converting text dates to pandas `datetime64`, plus stdlib `datetime` creation, formatting, parsing, and arithmetic | 36 |

*(`DateTime.py` is grouped here rather than under Language Basics — it's really a pandas + stdlib datetime file, not a core-language topic.)*

### Visualisation

| File | Covers | Lines |
|---|---|---|
| `Matplotlib.py` | Line plots, subplots, figures/axes, histograms, scatter plots, line styling | 112 |
| `Seaborn.py` | Dataset inspection (`columns`, `corr`, `value_counts`, `unique`) plus bar/box/cat/dis/heatmap/line/scatter/histogram plots on the `tips` dataset | 85 |

### Machine Learning

| File | Covers | Lines |
|---|---|---|
| `BalancingData.py` | Upsampling, downsampling, and SMOTE for an imbalanced binary target | 79 |
| `Encoding.py` | One-hot, label, and ordinal encoding of categorical columns | 70 |
| `FeatureEngineering.py` | Handling missing values with mean/median/mode imputation | 25 |
| `Sklearn.py` | A full linear regression pipeline: train/test split, feature scaling, training, evaluation metrics | 55 |

### Databases

| File | Covers | Lines |
|---|---|---|
| `SQL.py` | SQLite CRUD, `SELECT` variants (columns/limit/order/where), and aggregate functions (`count`/`avg`/`max`/`min`/`group by`) via `sqlite3` | 241 |

## Requirements

Install with `pip install -r requirements.txt`.

**Pure standard library, no install needed:** `Boolean.py`, `Input.py`, `Conditionals.py`, `Conversion.py`, `Numbers.py`, `Strings.py`, `Dictionary.py`, `List.py`, `Set.py`, `Tuple.py`, `Annotation.py`, `Functions.py`, `Module.py`, `OOP.py`, `ErrorHandling.py`, `Files.py`, `SQL.py`.

**Third-party:**

| Library | Used by |
|---|---|
| `numpy` | NumPy, Pandas, Matplotlib, Sklearn, BalancingData |
| `pandas` | Pandas, DateTime, Loops, Encoding, BalancingData |
| `matplotlib` | Matplotlib, Seaborn |
| `seaborn` | Seaborn, Loops, Matplotlib, Encoding, FeatureEngineering, Sklearn |
| `scikit-learn` | Encoding, BalancingData, Sklearn |
| `imbalanced-learn` | BalancingData |

## Data Files

Three files originally referenced local data that wasn't in the repo (`abc.csv`, `data.csv`, `excel.xlsx`/`excel_na.xlsx`/`csv_df*.csv`, and a broken `'...csv'` placeholder). Each was resolved one of two ways:

- **Generated fixtures in `data/`**, sized to match output comments that already existed in the file, verified by execution: `data/city_temperatures.xlsx`, `data/city_temperatures_missing.xlsx`, `data/employees.csv`, `data/employees_1.csv`, `data/employees_2.csv` (all `Pandas.py`), `data/support_tickets.csv` (`DateTime.py`).
- **Swapped to seaborn's built-in datasets** (`tips`, `titanic`), which need no local file: `Loops.py`, `Matplotlib.py`, `Sklearn.py` (all previously broken paths), plus `Seaborn.py`, `Encoding.py`, and `FeatureEngineering.py` (already used built-ins before this review).

`Module.py` had an analogous problem — it imported a `serhatmodule` package that didn't exist anywhere in the repo. A minimal stub package (`serhatmodule/__init__.py` + `serhatmodule/serhatsubmodule.py`) was added so the import examples run for real.

A few files create local artifacts when run (`SQL.py` → `database.db`, `Files.py` → `test.txt`, `Matplotlib.py` → `age_weight_plot.png`); all three are self-contained and covered by `.gitignore`.

## Conventions

- **`# Output: <value>`** appears after an expression to show what it evaluates to — read it in place of running the code.
- **`# Renders: <description>`** appears after a plotting call (`Matplotlib.py`, `Seaborn.py`) instead of `# Output:`, since a plot has no printable return value — it describes what the call draws.
- **`# === Section ===`** divides a file into named parts so you can jump to a topic within a file.
- **`# Behaviour varies by version: ...`** flags a result that depends on your installed library version (dtype names, scalar repr, sort order) rather than presenting one version's output as universal.

## Review Status

Every file in this repository was re-verified by actually running its code during this review, not by inspection alone — including files with no prior known issues, which turned up additional bugs in several cases (a wrong NumPy matrix sum, an inverted ordinal-encoding mapping, a mislabeled subplot title, a misdiagnosed `duplicated()` count, and others fixed along the way).

**"Verified" means:** outputs marked as verified were checked by execution against these exact library versions:

```
pandas            3.0.2
numpy             2.4.2
matplotlib        3.10.8
seaborn           0.13.2
scikit-learn      1.8.0
imbalanced-learn  0.14.1
```

If you're on different versions, expect differences in a few specific places that are called out inline wherever known: **dtype names** (e.g. pandas 3.x reports `dtype='str'` for string columns where older pandas reports `dtype='object'`), **scalar repr** (NumPy 2.x displays a bare integer result as `np.int64(5)` in a REPL, not plain `5`), and **`.info()` output** (memory usage and the printed class path both shift slightly by version). None of this affects the underlying values — only how they're displayed.

**Known gaps, honestly:**
- `Numbers.py` covers only `type()` on two values — an expansion (arithmetic operators, `round`/`abs`/`divmod`, floating-point precision) has been proposed and is pending approval as of this writing.
- This repository is a personal, evolving reference. It is not claimed to be a comprehensive Python or data-science course, and it will keep changing as more of it gets used and re-checked.

## License

MIT — see [LICENSE](LICENSE).

## Contact

Serhat Mercan
