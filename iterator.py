# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:
    # Constructor
    def __init__(self, limit):
        self.limit = limit

    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element
    def next(self):
        # Store current value of x
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x

# Prints numbers from 10 to 15
for i in Test(15):
    print(i)

# Print nothing
for i in Test(5):
    print(i)

# Sample built-in iterators
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a string
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = {'xyz':123, 'abc':345}
for i in d:
    print("%s %d" % (i, d[i]))
