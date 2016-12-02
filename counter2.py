# Python program to demonstrate accessing of
# Counter elements
from collections import Counter

# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
col_count = Counter(z)
print(col_count)

col = ['blue', 'red', 'yellow', 'green']

# Here green is not in col_count
# so count of green will be zero
for color in col:
    print(color, col_count[color])

# Python example to demonstrate elements() on
# Counter (gives back list)
coun = Counter(a=1, b=2, c=3)
print(coun)
print(list(coun.elements()))

# Python example to demonstrate most_elements() on
# Counter
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

# This prints 3 most frequent characters
for letter, count in coun.most_common(3):
    print('%s: %d' % (letter, count))
