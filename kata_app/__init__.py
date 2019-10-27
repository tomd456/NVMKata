"This constructor method is used to provide generic arithmatic endpoints for testing purposes."

def addition(arg):
    "This module provides testing endpoint for addition calculations"
    total = 0
    for val in arg:
        total += val
    return total

def difference(value1, value2):
    "This module provides addition endpoint for difference calculations"
    total = value1 - value2
    return total

def multiply(value1, value2):
    "This module provides addition endpoint for multiply calculations"
    total = value1 * value2
    return total

def division(value1, value2):
    "This module provides addition endpoint for division calculations"
    total = value1 / value2
    return total

def modulas(value1, value2):
    "This module provides addition endpoint for modulas calculations"
    total = value1 % value2
    return total
