# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.

# This first line is provided for you

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)
pay = rate * hrs
print("Pay:",pay)
