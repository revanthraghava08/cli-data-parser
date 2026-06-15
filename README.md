# CLI Data Parser

A command-line tool to read, filter, and analyse CSV data using Python.

## Features

- Reads any CSV file from the terminal
- Filters rows based on a minimum value for any numeric column
- Computes stats — average, highest, lowest, total, pass count
- Saves filtered rows to a new CSV file
- Handles all edge cases — missing file, wrong column, empty results

## Project Structure

```
cli-data-parser/
├── data/
│   └── students.csv
├── parser.py
├── requirements.txt
└── README.md
```

## Setup

```bash
# clone the repo
git clone https://github.com/revanthraghava08/cli-data-parser.git
cd cli-data-parser

# create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# basic run (defaults: column=marks, min=60)
python parser.py data/students.csv

# custom column and minimum value
python parser.py data/students.csv --column marks --min 75

# custom output file
python parser.py data/students.csv --min 80 --output data/toppers.csv
```

## Sample Output

```
Loaded 7 rows
=====Stats=====
Average: 69.86
Highest: 95.0
Lowest: 38.0
Total: 7
Passed Count: 4
===============
Filtering the rows where marks >= 60...
Saved 4 rows to data/output.csv
```

## Arguments

| Argument   | Default         | Description             |
|------------|-----------------|-------------------------|
| `file`     | required        | Path to input CSV       |
| `--column` | marks           | Column to analyse       |
| `--min`    | 60              | Minimum value to filter |
| `--output` | data/output.csv | Output file path        |

## Built With
- Python 3.14.2
- csv (built-in)
- argparse (built-in)
- os (built-in)