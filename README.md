# PYGuide — Python Reference Cookbook

Runnable Python snippets with their output written inline, covering language
basics through pandas, plotting and scikit-learn.

- **Runnable snippets** — one file per topic, each a flat list of independent examples.
- **Verified inline outputs** — every result is recorded as a `# Output:` comment, so you can read the answer without running anything.
- **Basics → data analysis → ML** — language fundamentals, data structures, NumPy, pandas, Matplotlib, Seaborn, scikit-learn, and SQLite.
- **A personal reference, not an application or a course** — there's no entry point and no CLI.

## Overview

This is a personal reference cookbook of Python snippets — my own notes, kept as short, readable examples with the expected result written inline as a comment. It is **not** a tutorial and **not** an application. Each file covers one topic as a flat list of independent snippets, meant to be looked up rather than worked through in order.

## What Makes It Different

- **Files are designed to run top to bottom where practical.** Most snippets are plain expressions whose result is recorded in a comment rather than printed, so running a file often produces little or no console output — but the files execute cleanly end to end rather than depending on missing local data.
- **Outputs are written inline as `# Output:` comments.** The result travels with the code, so the snippet is useful while reading a diff, a search result, or a single line pasted elsewhere.
- **Version-dependent output is marked, not glossed over.** Where a result depends on the installed library version — dtype names, scalar repr, sort order — the comment says so instead of presenting one version's output as universal. See [Verified Environment](#verified-environment).
- **Self-contained data.** Examples use either the small fixtures in `data/` or seaborn's built-in datasets, so nothing depends on files that only exist on one machine.

## How to Use

- Open the file for the topic you want (see the index below) and read top to bottom.
- Every snippet shows its result as a `# Output:` comment — you can read the answer without running anything.
- To find how a specific method or function is used, search for it by name across files (`grep`, your editor's project search, etc.) — that's the intended way to navigate this repo, not a table of contents.
- A few files load small fixture files from `data/`, or seaborn's built-in datasets (`tips`, `titanic`) — see **Data Files** below.

## Topic Index

Each row's description is drawn from what the file actually contains, not from its name. Line counts reflect the files as they currently stand.

### Language Basics

| File | Covers | Lines |
|---|---|---|
| `Boolean.py` | Defining a boolean and checking its type | 5 |
| `Input.py` | Reading user input with `input()` and building a greeting from it (sample session shown, since the real output depends on what you type) | 11 |
| `Conditionals.py` | Comparison/logical operators, `if`/`elif`/`else`, and membership tests (`in`/`not in`) across dict, list, set, and tuple | 38 |
| `Conversion.py` | Converting between `str`, `int`, and `float` | 8 |
| `Loops.py` | `break`/`continue`, `for` loops over lists, dicts, sets, tuples, and DataFrame columns, and `while` loops | 82 |
| `Numbers.py` | `type()` on `float` and `int` | 6 |
| `Strings.py` | Indexing, slicing, and common string methods (`capitalize`, `count`, `split`, `upper`) | 45 |

### Data Structures

| File | Covers | Lines |
|---|---|---|
| `Dictionary.py` | Creating dictionaries, accessing keys/values, `.get()` with a default, adding entries | 26 |
| `List.py` | Indexing, slicing, comprehensions, and common list methods (`append`, `insert`, `pop`, `sort`, `reverse`) | 63 |
| `Set.py` | Creating sets, union, intersection, and converting a list to a set to drop duplicates | 25 |
| `Tuple.py` | Creating tuples, indexing, `count()`, and `index()` on an immutable sequence | 17 |

### Functions & Structure

| File | Covers | Lines |
|---|---|---|
| `Annotation.py` | Variable, function, class, and list type annotations, including the modern `list[int]` generic and `int \| str` union syntax | 49 |
| `Functions.py` | Default arguments, `*args`/`**kwargs`, `enumerate`, `filter`, `lambda`, `map`, `random`, `range`, `zip` | 97 |
| `Module.py` | Importing a module, a name from it, and a submodule three different ways, backed by a small local stub package (`serhatmodule/`) so the example actually runs | 25 |
| `OOP.py` | Classes, inheritance, encapsulation, polymorphism, and abstraction via `abc.ABC` | 109 |
| `ErrorHandling.py` | `try`/`except`, `else`, `finally`, `raise`, and custom exceptions | 52 |
| `Files.py` | Writing, reading, and appending to a local text file | 20 |

### Data Analysis

| File | Covers | Lines |
|---|---|---|
| `NumPy.py` | Array creation, indexing/slicing, arithmetic, matrix operations, random arrays, linear algebra | 128 |
| `Pandas.py` | Series and DataFrame creation, `.loc`/`.iloc`, Excel/CSV I/O, missing-data handling, `groupby`, `concat`/`merge`, `.apply()` — the deepest file in the repo | 666 |
| `DateTime.py` | Converting text dates to pandas `datetime64`, plus stdlib `datetime` creation, formatting, parsing, and arithmetic | 37 |

*(`DateTime.py` is grouped here rather than under Language Basics — it's really a pandas + stdlib datetime file, not a core-language topic.)*

### Visualisation

| File | Covers | Lines |
|---|---|---|
| `Matplotlib.py` | Line plots, subplots, figures/axes, histograms, scatter plots, line styling | 112 |
| `Seaborn.py` | Dataset inspection (`columns`, `corr`, `value_counts`, `unique`) plus bar/box/cat/dis/heatmap/line/scatter/histogram plots on the `tips` dataset | 86 |

### Machine Learning

| File | Covers | Lines |
|---|---|---|
| `BalancingData.py` | Upsampling, downsampling, and SMOTE for an imbalanced binary target | 89 |
| `Encoding.py` | One-hot, label, and ordinal encoding of categorical columns | 80 |
| `FeatureEngineering.py` | Handling missing values with mean/median/mode imputation | 31 |
| `Sklearn.py` | A full linear regression pipeline: train/test split, feature scaling, training, evaluation metrics | 56 |

### Databases

| File | Covers | Lines |
|---|---|---|
| `SQL.py` | SQLite CRUD, `SELECT` variants (columns/limit/order/where), and aggregate functions (`count`/`avg`/`max`/`min`/`group by`) via `sqlite3` | 242 |

## Getting Started

Requires **Python 3.10+** (`Annotation.py` uses `list[int]` and `int | str` syntax).

```bash
git clone https://github.com/serhatmercan/PYGuide.git
cd PYGuide
pip install -r requirements.txt
```

- **Run scripts from the repository root** — files that read fixtures use relative paths such as `data/employees.csv`, so they will not find their data from another working directory.
- **For headless plotting**, set the non-interactive Matplotlib backend: `MPLBACKEND=Agg python Matplotlib.py`. Under `Agg` the `plt.show()` calls emit a harmless "non-interactive" warning instead of opening a window.
- Running a few files creates local artifacts — `SQL.py` → `database.db`, `Files.py` → `test.txt`, `Matplotlib.py` → `age_weight_plot.png`. All three are gitignored.

## Requirements

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

Every example is self-contained. Data comes from one of two places:

- **Small synthetic fixtures committed to `data/`**, generated for these examples and containing no real-world data: `city_temperatures.xlsx`, `city_temperatures_missing.xlsx`, `employees.csv`, `employees_1.csv`, `employees_2.csv` (all used by `Pandas.py`), and `support_tickets.csv` (`DateTime.py`).
- **seaborn's built-in datasets** (`tips`, `titanic`), which download nothing and need no local file: `Loops.py`, `Matplotlib.py`, `Seaborn.py`, `Encoding.py`, `FeatureEngineering.py`, `Sklearn.py`.

`Module.py`'s import examples are backed by the small `serhatmodule/` package in this repository (`__init__.py` + `serhatsubmodule.py`), so the module, name, and submodule imports it demonstrates all resolve for real.

## Conventions

- **`# Output: <value>`** appears after an expression to show what it evaluates to — read it in place of running the code.
- **`# Renders: <description>`** appears after a plotting call (`Matplotlib.py`, `Seaborn.py`) instead of `# Output:`, since a plot has no printable return value — it describes what the call draws.
- **`# === Section ===`** divides a file into named parts so you can jump to a topic within a file.
- **`# Behaviour varies by version: ...`** flags a result that depends on your installed library version (dtype names, scalar repr, sort order) rather than presenting one version's output as universal.

## Verified Environment

Inline outputs are checked by running the code, not by inspection. The values recorded in `# Output:` comments were produced against these library versions:

```
pandas            3.0.2
numpy             2.4.2
matplotlib        3.10.8
seaborn           0.13.2
scikit-learn      1.8.0
imbalanced-learn  0.14.1
```

If you're on different versions, expect differences in a few specific places that are called out inline wherever known: **dtype names** (e.g. pandas 3.x reports `dtype='str'` for string columns where older pandas reports `dtype='object'`), **scalar repr** (NumPy 2.x displays a bare integer result as `np.int64(5)` in a REPL, not plain `5`), and **`.info()` output** (memory usage and the printed class path both shift slightly by version). None of this affects the underlying values — only how they're displayed.

## Scope & Limitations

- **Coverage is uneven by design.** `Pandas.py` is a deep reference; `Numbers.py` covers only `type()` on two values. Depth follows what has actually been needed, not a syllabus.
- **This is a personal, evolving reference**, not a comprehensive Python or data-science course. It will keep changing as more of it gets used and re-checked.
- **The machine-learning files are syntax references, not modelling advice.** They demonstrate individual steps — encoding, imputation, resampling, a regression pipeline — and each notes inline where a real workflow would order things differently to avoid leaking test data.
- **Verification is local script execution only.** There is no test suite and no CI in this repository.

## License

MIT — see [LICENSE](LICENSE).

## Author

Serhat Mercan — [github.com/serhatmercan](https://github.com/serhatmercan)
