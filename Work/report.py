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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except ValueError:
                print(f"Couldn't parse line: {row}")
            except IndexError:
                print(f"Missing data in row: {row}")

    return prices

# Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.

def make_report(portfolio, prices):
    report = []
    for entry in portfolio:
        temp = (
            entry["name"],
            entry["shares"],
            prices[entry["name"]],
            prices[entry["name"]] - entry["price"]
        )
        report.append(temp)
    return report

def main():
    portfolio = read_portfolio("Work/Data/portfolio.csv")
    prices = read_prices("Work/Data/prices.csv")
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price($)', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(("-"*10+" ")*4)

    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

main()
