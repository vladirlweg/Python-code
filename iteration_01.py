# Write a program which repeatedly reads integers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the integers.
# If the user enters anything other than an integer, detect their mistake using
# try and except and print an error message and skip to the next integers.
# Print also the maximum and minimum of the numbers.

count = 0
total = 0

maximum = None
minimum = None

while True:
    # input from user
    number = input('Enter a number: ')
    
    # if user input done then the program stops
    if number.lower() == 'done':
        if count>0:
            # average
            avg = total/count
            print('Total:', total, 'Count:', count, 'Average:', avg, 'Minimum', minimum, 'Maximum:', maximum)
        else:
            print('No valid integers were added')
        break
    
    try:
        fnumber = float(number)
        total = total+fnumber
        count = count+1
        
        #minimum
        if minimum is None or fnumber<minimum:
            minimum = fnumber
        #maximum
        if maximum is None or fnumber>maximum:
            maximum = fnumber
    except:
        print('Invalid input')
        continue
    
    