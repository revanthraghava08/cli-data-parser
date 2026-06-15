# 1. Getting the filename from the terminal
#===========================================
# 2. Read the CSV file
#===========================================
# 3. Filtering the rows where the marks >= some value
#===========================================
# 4. Computing the stats (average, min, max, pass count)
#===========================================
# 5. Printing the stats
#===========================================
# 6. Saving the filtered data to a new CSV file
#===========================================

import csv
import sys
import argparse
import os

class DataParser:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def load(self):
        try:
            with open(self.filepath) as f:
                self.data = list(csv.DictReader(f))
            if not self.data:
                print("Error: CSV file is empty.")
                sys.exit(1)
            print(f"Loaded {len(self.data)} rows")
        except FileNotFoundError:
            print(f"Error: '{self.filepath}' not found.")
            sys.exit(1)

    def validate_column(self, column):
        if column not in self.data[0]:
            print(f"Error: Column '{column}' not found.")
            available = ", ".join(self.data[0].keys())
            print(f"Available Columns: {available}")
            sys.exit(1)
        try:
            [float(r[column]) for r in self.data]
        except ValueError:
            print(f"Error: Column '{column}' contains text, not numbers.")
            print("Numeric columns only")
            sys.exit(1)

    def filter_rows(self, column, min_value):
        return [r for r in self.data if float(r[column]) >= min_value]
    
    def stats(self, column, min_value):
        vals = [float(r[column]) for r in self.data]
        return {
            "Average" : round(sum(vals) / len(vals) , 2),
            "Highest" : max(vals),
            "Lowest" : min(vals),
            "Total" : len(vals),
            "Passed Count" : len([v for v in vals if v >= min_value])
        }
    
    def save(self, rows, output_path):
        if not rows:
            print("No rows matched. Nothing saved.")
            return
        dir_name = os.path.dirname(output_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Saved {len(rows)} rows to {output_path}")

def get_args():
    parser = argparse.ArgumentParser(description="CSV Data Parser")
    parser.add_argument("file", help="Path to input CSV")
    parser.add_argument("--column", default="marks", help="Column to analyse")
    parser.add_argument("--min", type=float, default=60, help="Minimum value")
    parser.add_argument("--output", default="data/output.csv", help="Output file")
    return parser.parse_args()
    
if __name__ == "__main__":
    args = get_args()

    p = DataParser(args.file) 
    p.load()
    p.validate_column(args.column)

    s = p.stats(args.column, args.min)
    print(f"=====Stats=====")
    print(f"Average: {s['Average']}")
    print(f"Highest: {s['Highest']}")
    print(f"Lowest: {s['Lowest']}")
    print(f"Total: {s['Total']}")
    print(f"Passed Count: {s['Passed Count']}")
    print(f"===============")

    print(f"Filtering the rows where {args.column} >= {args.min}...")
    filtered = p.filter_rows(args.column, args.min)
    p.save(filtered, args.output)