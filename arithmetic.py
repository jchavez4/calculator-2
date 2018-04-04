# """Math functions for calculator."""


# def add(num1, num2):
#     """Return the sum of the two inputs."""
#     return num1 + num2


# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""

#     return num1 - num2


# def multiply(num1, num2):
#     """Multiply the two inputs together."""

#     return num1 * num2


# def divide(num1, num2):
#     """Divide the first input by the second and return the result."""

#     return num1/num2


# def square(num1):
#     """Return the square of the input."""

#     return num1 ** 2


# def cube(num1):
#     """Return the cube of the input."""

#     return num1 ** 3


# def power(num1, num2):
#     """Raise num1 to the power of num2 and return the value."""

#     return num1 ** num2


# def mod(num1, num2):
#     """Return the remainder of num1 / num2."""

#     return num1 % num2


# def add_mult(num1, num2, num3):
#     """Return the result of adding num1 and num2 multiplied by num3."""

#     return (num1 + num2) * num3


# def add_cubes(num1, num2):
#     """Return the result of adding the cubes of num1 and num2."""

#     return cube(num1) + cube(num2)

def add(num_list):
    """Returns sum of numbers in the list."""
    
    sum = 0
    for num in num_list:
        sum += num
    return sum


def subtract(num_list):
    """Returns the difference of numbers in the list."""
    
    difference = num_list[0]
    for i in range(1, len(num_list)):
        difference -= num_list[i]
    return difference


def multiply(num_list):
    """Returns the product of numbers in the list."""
    
    product = num_list[0]
    for i in range(1, len(num_list)):
        product *= num_list[i]
    return product


def divide(num_list):
    """Returns the result of numbers in list divided."""
    
    result = num_list[0]
    for i in range(1, len(num_list)):
        result /= num_list[i]
    return result


def square(num_list):
    """Returns the square of the number in the list."""

    return num_list[0] ** 2


def cube(num_list):
    """Returns the cube of the number in the list."""

    return num_list[0] ** 3

def power(num_list):
    """Returns the first number raised to the power of the second number in list."""

    return num_list[0] ** num_list[1]

def mod(num_list):
    """Returns the remainder of first number/second number"""

    return num_list[0] % num_list[1]
# print add([5,2,3])
# print subtract([5,10,10])
# print multiply([1, 2, 3])
# # print divide([10, 2])
# print square([5])
# print cube([2])
print power([2, 3])
print mod([10, 5])