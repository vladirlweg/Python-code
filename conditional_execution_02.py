# Write a program to prompt the user for hours and rate per hour to compute
# gross pay. Moreover the employee that work more than 40h should be paid
# 1.5 times the hourly rate.
# This time the program should use "try" and "except" so that your program
# handles non-numeric input gracefully by printing a message and exiting
# the program.

# function to calculate total payment
def computepay(hours, rate):
    if hours > 40:
        regular = 40*rate
        overtime = (hours-40)*(rate*1.5)
        total = regular + overtime
    else:
        total = hours*rate
    return total


while True:
    # input hours from user
    hours = input('Hours: ')
    
    # if user input done then the program stops
    if hours.lower() == 'done':
        break
    
    #input rate from user
    rate = input('Rate: ')
    
    # if user input done then the program stops
    if rate.lower() == 'done':
        break

    # convert hours from character variable to float variable
    try:
        fhours = float(hours)
        frate = float(rate)
    except:
        print('Invalid input')
        continue
        
    # calculate total payment
    pay = computepay(fhours, frate)
        
    # print total payment
    print('Pay:', pay)
