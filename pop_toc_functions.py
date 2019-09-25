# Define functions for POPTOC here

# Write some sudo code

def num1(arg):
    if arg%3 == 0 and arg%5 == 0:
        return 'POPTOC'
    else:
        return (f'{arg} is not divisible by 3 and 5')

def num2(arg):
    if arg%5 == 0:
        return 'TOC'
    else:
        return (f'{arg} is not divisible by 5')

def num3(arg):
    if arg%3 == 0:
        return 'POP'
    else:
        return (f'{arg} is not divisible by 3')

