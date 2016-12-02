# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

# A Python program to demonstrate use of
# generator object with next()
# A generator function
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.next())
print(x.next())
print(x.next())

# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

# Create a generator object
x = fib(5)
# Iterating over the generator object using next
print(x.next())
print(x.next())
print(x.next())
print(x.next())
print(x.next())
# Iteration over the generator object using for
# in loop
print("\nUsing for in loop")
for i in fib(5):
    print(i)
