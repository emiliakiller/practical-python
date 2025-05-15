# report.py
# Write a function read_prices(filename) that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
# Exercise 2.4

import csv

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

def read_prices(filename):
    '''Reads a list of prices and stores them in a dictionary of ticker symbols'''
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            print(row)
            try:
                prices[row[0]] = float(row[1])
            except ValueError:
                print(f"Couldn't parse line {row}")
            except IndexError:
                print(f"Missing data in row {row}")

    return prices
