# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage
# Exercise 1.7

# Assumptions: 5% interest rate is monthly, monthly payment is the entire payment

def main(mortgage_value, mortgage_duration, monthly_interest_rate, monthly_payment):
    return (mortgage_duration * 12 * monthly_payment)

print(main(500000, 30, 0.05, 2684.11))
