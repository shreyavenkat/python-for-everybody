# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
diff = hrs - 40
if diff > 0:
    base = 40 * rate
    tax = rate * 1.5 * diff
else:
    base = hrs * rate
    tax = 0
total = base + tax
print(total)
