# Create a new dictionary
d = dict() # or d = {}

# Add a key - value pairs to dictionary
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary
print d

# print only the keys
print d.keys()

# print only vlaues
print d.values()

# iterate over dictionary
for i in d:
    print("%s %s" % (i, d[i]))

# another method of iteration
for index, value in enumerate(d):
    print index, value, d[value]

# check if key exist
print 'xyz' in d

# delete the key-value pair
del d['xyz']

# check again
print 'xyz' in d

# Function to illustrate break in loop
def breakTest(arr):
    for i in arr:
        if i == 5:
            break
        print i,
        # For new line
    print

# Function to illustrate continue in loop
def continueTest(arr):
    for i in arr:
        if i == 5:
            continue
        print i,

    # For new line
    print

# Function to illustrate pass
def passTest(arr):
    pass

# Driver program to test above functions
# Array to be used for above functions:
arr = [1, 3, 4, 5, 6, 7]

#Illustrate break
print "Break method output"
breakTest(arr)

# Illustrate continue
print "Continue method output"
continueTest(arr)

# Illustrate pass- Does nothing
passTest(arr)

# Python program to test map, filter and lambda

# Function to test map
def cube(x):
    return x ** 2

# Driver to test above function
# Program for working of map
print("MAP EXAMPLE")
cubes = map(cube, range(10))
print(cubes)

print("LAMBDA EXAMPLE")

# first parentheses contains a lambda form, that is
# a squaring function and second parentheses represents
# calling lambda
print(lambda x: x ** 2)(5)

# Make function of two arguments that return their product
print(lambda x, y: x*y)(3, 4)

print("FILTER EXAMPLE")
special_cubes = filter(lambda x: x > 9 and x < 60, cubes)
print(special_cubes)

# code without using map, filter and lambda

# Find the number which are odd in the list
# and multiply them by 5 and create a new list
# Declare a new list
x = [2, 3, 4, 5, 6]
# Empty list for answer
y = []
# Perform the operations and print the answer
for v in x:
    if v % 2:
        y += [v*5]

print(y)

# The same operation can be performed in two lines using map, filter and lambda
x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
print(y)
