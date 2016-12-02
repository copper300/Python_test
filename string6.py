# Python code to demonstrate working of
# strp(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print(" String after stripping all '-' is : %s" % str.strip('-'))

# using lstrip() to delete all trailing '-'
print(" String after stripping all trailing '-' is : %s" % str.rstrip('-'))

# using rstrip() to delete all leading '-'
print(" String after stripping all leading '-' is : %s" % str.lstrip('-'))

# Python code to demonstrate working of
# min() and max()
str = "geeksforgeeks"

# using min() to print the smallest character
# prints 'e'
print("The minimum value character is : %s" % min(str))

# using max() to print the largest character
# prints 's'
print("The maximum value character is : %s" % max(str))

# Python code to demonstrate working of
# maketrans() and translate()
from string import maketrans # for maketrans()
str = "geeksforgeeks"
str1 = "gfo"
str2 = "abc"

# using maketrans() to map elements of str2 with str1
mapped = maketrans(str1, str2)

# using translate() to translate using the mapping
print("The string after translation using mapped elements is : %s" % str.translate(mapped))

# Python code to demonstrate working of
# replace()
str = "nerdsfornerds is for nerds"
str1 = "nerds"
str2 = "geeks"
# using replace() to replace str2 with str1 in str
# only changes 2 occurences
print("The string after replacing string is : %s" % str.replace(str1, str2))
