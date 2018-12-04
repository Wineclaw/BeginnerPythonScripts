# A simple compounding interest script that prints the final compounded amount
# after asking the user for inputs.
#
# By: Wineclaw, December 4, 2018

# Asks user for information

P = int(input("What is the principal amount?"))
r = float(input("What is the interest rate (in decimals)?"))
n = int(input("How many times per year is the interest compounded?"))
t = int(input("How many years will the money be compounded for?"))

# Final amount equation

final_amount = P * (1 + (r/n)) ** (n*t)

# prints final amount after t years

print("The final amount after", t, "years is $", final_amount)