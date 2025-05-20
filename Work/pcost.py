# pcost.py
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
# Exercise 1.27

import report
import sys

records = []

def portfolio_cost(filename):
    '''Calculates the total value of a portfolio from a csv file representing the portfolio'''
    # Modify the pcost.py file so that it uses the report.read_portfolio() function.
    total_cost = 0

    portfolio = report.read_portfolio(filename)
    total_cost = sum([s['price']* s['shares'] for s in portfolio])

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
