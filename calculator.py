"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
# function that tokenizes input str
# function calculator_loop

from arithmetic import *


# Your code goes here
def tokenize_input(input_str):
    """this will return the split input str"""
    return input_str.split(" ")


def calculator():
    """Performs different arithmetic based on user input."""
    while True:
        user_input = raw_input("Enter desired arithmetic: ")
        tokens = tokenize_input(user_input)
        if tokens[0] == "q" or tokens[0] == "quit":
            return
        else:
            if tokens[0] == "+":
                print add(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "-":
                print subtract(int(tokens[1]), int(tokens[2]))


calculator()         