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
    
    int_list = []
    split_str = input_str.split(" ")
    for i in range(1, len(split_str)):
        int_list.append(float(split_str[i]))
    return split_str[0], int_list


def calculator():
    """Performs different arithmetic based on user input."""
    while True:
        user_input = raw_input("Enter desired arithmetic: ")
        tokens = tokenize_input(user_input)
        if tokens[0] == "q" or tokens[0] == "quit":
            return
        else:
            if tokens[0] == "+":
                print reduce(lambda x, y: add(x,y), tokens[1])
            elif tokens[0] == "-":
                print reduce(lambda x, y: subtract(x,y), tokens[1])
            elif tokens[0] == "*":
                print reduce(lambda x, y: multiply(x,y), tokens[1])
            elif tokens[0] == "/":
                    print reduce(lambda x, y: divide(x,y), tokens[1])
            elif tokens[0] == "square":
                if len(tokens[1]) > 1:
                    print "Square only takes one number."
                else:
                    print square(tokens[1])
            elif tokens[0] == "cube":
                if len(tokens[1]) > 1:
                    print "Cube only takes one number."
                else:
                    print cube(tokens[1])
            elif tokens[0] == "pow":
                if len(tokens[1]) > 2:
                    print "Pow only takes two numbers."
                else:
                    print power(tokens[1])
            elif tokens[0] == "mod":
                if len(tokens[1]) > 2:
                    print "Mod only takes two numbers."
                else:
                    print mod(tokens[1])
            else:
                print "Please enter valid command."


calculator()
