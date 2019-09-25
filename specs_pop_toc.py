# Dont forget to import functions
from pop_toc_functions import *
# Run some tests here


# Write a test to check of divisible by 3
print('////////////////////////////////////////')
print("Testing POPTOC, with arg with a number divisible by three -- > POP")
print(num3(arg=3) == 'POP')
print(num3(arg = 3))
print('////////////////////////////////////////')

# Write a test to check if divisible by 5
print("Testing POPTOC, with arg with a number divisible by five -- > TOC")
print(num2(arg=5) == 'TOC')
print(num2(arg = 5))
print('////////////////////////////////////////')

# Write a test to check if its devisible by 5 and 3
print("Testing POPTOC, with arg as a number divisible by three and five -- > POPTOC")
print(num1(arg= 15) == 'POPTOC')
print(num1(arg = 15))
print('////////////////////////////////////////')
