# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage
# Exercise 1.7

# Assumptions: 5% interest rate is annual, monthly payment is the entire payment

# Fixed-Rate Mortgage Formula (from https://www.wallstreetprep.com/knowledge/fixed-rate-mortgage/ )
# The formula to calculate the monthly payment for a fixed-rate mortgage is as follows:

# Monthly Payment = [P × r × (1 + r)^n] ÷ [(1 + r)^n – 1]
# Where:

# P → Principal Loan Amount
# r → Monthly Interest Rate (Annual Interest Rate ÷ 12)
# n → Number of Payments (Borrowing Term in Years × 12)

def main(mortgage_value, mortgage_duration, annual_interest_rate, monthly_payment):
    total_paid = 0
    while mortgage_value > 0:
        mortgage_value *= (1+annual_interest_rate/12)
        mortgage_value -= monthly_payment
        total_paid += monthly_payment
    return total_paid

print(main(500000, 30, 0.05, 2684.11))
