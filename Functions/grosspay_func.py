# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Do not name your variable sum or use the sum() function.

def computepay(h,r):
    diff = h - 40
    if diff > 0:
        base = 40 * r
        tax = diff * r * 1.5
    else:
        base = h * r
        tax = 0
    total = base + tax
    return total

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)
