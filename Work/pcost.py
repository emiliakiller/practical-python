# pcost.py
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
# Exercise 1.27

import csv
import sys

records = []

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:

            try:
                records.append((row[0], int(row[1]), float(row[2])))
                total_cost += (int(row[1])*float(row[2]))
            except ValueError:
                print(f"Couldn't parse line {row}")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
