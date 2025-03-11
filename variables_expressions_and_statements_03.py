# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted
# temperature.

# input from the user
temp_Celsius = input("Give the temperature in Celsius: ")

# convert the character variable to float variable
temp_Celsius = float(temp_Celsius)

# convert the temperature to Fahrenheit
temp_Farenheit = (temp_Celsius*9/5)+32

# print the temperature
print("The temperature in Fahrenheit is:", temp_Farenheit)