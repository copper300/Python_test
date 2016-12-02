# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items
print Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])

# With dictionary
print Counter({'A':3, 'B':5, 'C':2})

# With keyword arguments
print Counter(A=3, B=5, C=2)

# A Python program to demonstrate update()
coun = Counter()
coun.update([1,2,3,1,2,1,1,2])
print(coun)
coun.update([1,2,4])
print(coun)

# Python program to demonstrate that counts in
# Counter can be 0 and negative
c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
c1.subtract(c2)
print(c1)

# An example program where different list items are
# counted using counter
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# Count distinct elements and print Counter object
print(Counter(z))
