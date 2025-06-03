#Task 2: Using the Math Module for Calculations

#Write a Python program that:
#1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
num = float(input('Enter a number: '))

square_root = math.sqrt(num)
logarithm = math.log(num)
sine = math.sin(num)

print("The square root of the number is:", square_root)
print("The natural logarithm (ln) of the number is:", logarithm)
print("The sine of the number (in radians) is:", sine)
