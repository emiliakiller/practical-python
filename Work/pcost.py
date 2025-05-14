# pcost.py
# The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0

    with open("Work/Data/portfolio.csv", "rt") as f:
       _ = next(f).split(',')
       for line in f:
           row = line.split(',')
           total_cost += (int(row[1])*float(row[2]))

    return total_cost

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost:', cost)
