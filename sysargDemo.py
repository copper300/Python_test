# Python code to demonstrate the use of 'sys' module
import sys

# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
print argumentList

# print the name of file
print(sys.argv[0])

# print the first argument after the name of file
# print(sys.argv[1])

# from math import factorial
# print(factorial(int(sys.argv[1])))

# Python program to illustrate the use of args which
# multiplies all the values given to the function as parameter
def multiplyAll(*values):
    mul = 1

    # values(args) will be in the form of tuple
    print values
    print("Type = ", type(values))

    # Multiplying the all the parameters and return the result
    for i in values:
        mul = mul * i

    return mul

# Driver program to test above function
ans = multiplyAll(1,2)
print("The multiplication of 1 and 2 is %d" % (ans))

ans = multiplyAll(3, 4, 5, 6, 7)
print("The multiplication of 3 to 7 is %d" % (ans))

# Program to illustrate the use of kwargs in Python

# Function that print the details of a student
# The number of details per student may vary
def printDetails(**details):
    # Variable 'details' contains the details in the
    # form of dictionary
    print("Parameter details contains")
    print(details)
    print("Type = ", type(details))

    # Print first name
    print("First name = %s" % (details['firstname']))
    # Print the department of student
    print("Department = %s" % (details['department']))

# Calling the function with three arguments
printDetails(firstname = "Nikhil", rollNumber = "007", department = "CSE")
# Calling the function with two arguments
printDetails(firstname = "Abhay", department = "ECE")

# Function contains both args and kwargs
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Burger", "It's very funny, sir.",
           "It's really very, VERY funny, sir.",
           shopkeeper="Micheal Palin",
           client="Jhon Cleese",
           sketch="Cheese Shop Sketch")
