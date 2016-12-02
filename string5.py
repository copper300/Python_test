# Python code to demonstrate working of
# len() and count()
str = "geeksforgeeks is for geeks"

# Printing length of string using len()
print(" The length of string is : %d" % len(str))

# Printing occurrence of "geeks" in string
# Printing 2 as it only checks till 15th element
print(" Number of appearance of ""geeks"" is : %d" % str.count("geeks", 0, 15))

# Python code to demonstrate working of
# centre(), ljust() and rjust()
str = "geeksforgeeks"

# printing the string after centering with '-'
print("The string after centering with '-' is : %s" % str.center(20, '-'))

# printing the string after ljust()
print("The string after ljust is : %s" % str.ljust(20, '-'))

# printing the string after rjust()
print("The string after rjust is : %s" % str.rjust(20, '-'))

# Python code to demonstrate working of
# isalpha(), isalnum(), isspace()
str = "geeksforgeeks"
str1 = "123"

# Checking if str has all alphabets
if (str.isalpha()):
    print("All characters are alphabet in str")
else:
    print("All characters are not alphabets in str")

# Checking if str1 has all numbers
if (str1.isalnum()):
    print("All characters are numbers in str1")
else:
    print("All character are not numbers in str1")

# Checking if str1 has all spaces
if (str1.isspace()):
    print("All characters are spaces in str1")
else:
    print("All characters are not spaces in str1")

# Python code to demonstrate working of
# join()
str = "_"
str1 = ("geeks", "for", "geeks")

#using join() to join sequence str1 with str
print("The string after joining is %s" % str.join(str1))
