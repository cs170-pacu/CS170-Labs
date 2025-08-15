################################################################################
# File name:    main.py
# Author:       YOUR NAME HERE
# Date:         5/14/2025
# Class:        CS 170-XX (replace XX with your section number)
# Assignment:   Pay Calculator
# Purpose:      Calculates the user's pay based on an hourly wage and the
#               number of hours worked
# Hours:        0.5
################################################################################

# Get number of hours worked
hours = float(input('How many hours did you work? '))

# Get the hourly pay rate
rate = float(input('How much did you get paid per hour? '))

# Calculate pay
pay = hours * rate

# Display the pay

print(f'You have earned $ {pay:.2f}')