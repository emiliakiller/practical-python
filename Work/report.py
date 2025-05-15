# report.py
# Using this code as a rough guide, create a new file report.py. In that file, define a function read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples. To do this, you’re going to make a few minor modifications to the above code.
# Exercise 2.4

import csv, sys

def read_portfolio(filename):
    '''Creates a list of tuples detailing a portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

portfolio = read_portfolio(filename)
print(f"Portfolio: {portfolio}")
