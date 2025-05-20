# fileparse.py
#
# Exercise 3.3
#
import csv

def parse_csv(filename:str, select: list | None=None, types: list | None=None, has_headers:bool=True, delimiter:str=",", silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            try:
                indices = [headers.index(colname) for colname in select]
                headers = select
            except ValueError:
                indices = []
                if not silence_errors:
                    raise RuntimeError("select argument requires column headers")
        else:
            indices = []

        records = []
        for rowno, row in enumerate(rows, 1):
            try:
                if not row:    # Skip rows with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]

                if types:
                    row = [ func(val) for func, val in zip(types, row) ]
                # Make a dictionary, otherwise a tuple if no headers
                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Error converting row {row}, reason: {e}")

    return records
