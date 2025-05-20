# report.py
# Write a function read_prices(filename) that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
# Exercise 2.4

# Modify the report.py program you wrote in Section 2.3 so that it uses the same technique to pick out column headers.

from fileparse import parse_csv

def read_portfolio(filename:str) -> list:
    '''Creates a list of tuples detailing a portfolio'''
    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str,int,float])
    return portfolio

def read_prices(filename:str) -> dict:
    '''Reads a list of prices and stores them in a dictionary of ticker symbols'''
    prices = {name:price for name,price in parse_csv(filename, types=[str,float], has_headers=False)}
    return prices

# Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.

def make_report(portfolio:list, prices:dict) -> list:
    '''
    Takes in a list of records from a portfolio, updates the price, calculates the change in the price, and returns a report in the form of a list
    '''
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

def portfolio_report(portfolio_filename:str, price_filename:str) -> None:
    '''
    Takes in the filenames of a portfolio and a pricelist, and compiles and prints a report of the information
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(price_filename)
    report = make_report(portfolio, prices)

    headers = ('Name', 'Shares', 'Price($)', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(("-"*10+" ")*4)

    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

# portfolio_report("Work/Data/portfoliodate.csv","Work/Data/prices.csv")
