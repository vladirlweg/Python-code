# Write a program to prompt the user for hours and rate per hour to compute
# gross pay.

#input from the user
hours = input("Enter hours: ")
rate = input("Enter rate: ")

# change character variables to float variables
hours_float = float(hours)
rate_float = float(rate)

# payment
pay = rate_float*hours_float

# print payment
print("Pay:", pay)
