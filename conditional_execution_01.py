# Write a program to prompt the user for hours and rate per hour to compute
# gross pay. Moreover the employee that work more than 40h should be paid
# 1.5 times the hourly rate.


# function to calculate total payment
def computepay(hours, rate):
    if hours > 40:
        regular = 40*rate
        overtime = (hours-40)*(rate*1.5)
        total = regular + overtime
    else:
        total = hours*rate
    return total

#input from the user
h = input("Enter hours: ")
r = input("Enter rate: ")

# convert character variables to float variables
h = float(h)
r = float(r)

# calculate total payment
pay = computepay(h,r)

# print total payment
print("Pay:", pay)
