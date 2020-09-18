#30 years is typical mortgage. That is 360 months.

months = int(input("Enter mortgage term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(input("Enter loan value: "))

monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan

print("The monthly payment for a loan of $%.2f for a %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (months / 12), rate, payment))