# report.py
# Take the function you wrote in Exercise 2.4 and modify to represent each stock in the portfolio with a dictionary instead of a tuple. In this dictionary use the field names of “name”, “shares”, and “price” to represent the different columns in the input file.
# Exercise 2.4

import csv, sys

def read_portfolio(filename):
    '''Creates a list of tuples detailing a portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

portfolio = read_portfolio(filename)
print(f"Portfolio: {portfolio}")
