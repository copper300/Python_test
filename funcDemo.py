# A python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.

# Adds a welcome message to the string
def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to"

    # Return concatenation of addWelcome()
    # and str
    return addWelcome() + str

# To get site name to which welcome is added
def site(site_name):
    return site_name

print(messageWithWelcome(site('GeeksforGeeks')))

# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome()
def decorate_message(fun):
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)

    # Decorator returns a function
    return addWelcome
@decorate_message
def site(site_name):
    return site_name

# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks"))

# A Python example to demonstrate that
# decorators can be useful attach data

# A decorator function to attach
# data to func
def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x, y):
    return x + y

# This call is equivalent to attach_data()
# with add() as parameter
print(add(2,3))
print(add.data)

# A python program to return multiple
# values from a method using class
class Test:
    def __init__(self):
        self.str = "geeksforgeeks"
        self.x = 20

# This function returns an object of Test
def fun():
    return Test()

t = fun()
print(t.str)
print(t.x)

# A python program to return multiple
# values from a method using tuple
# This functon returns a tuple
def fun():
    str = "geeksforgeeks"
    x = 20
    return str, x # Return tuple, we could also
                  # write(str, x)

str, x = fun()
print(str)
print(x)

# A Python program to return multiple
# values from a method using list
# This function returns a list
def fun():
    str = "geeksforgeeks"
    x = 20
    return [str, x]

list = fun()
print(list)

# A Python program to returm multiple
# values from a method using dictionary
# This function returns a dictionary
def fun():
    d = dict()
    d['str'] = "geeksforgeeks"
    d['x'] = 20
    return d

d = fun()
print(d)
