# Python code to demonstrate working of
# find() and rfind()
str = "geekforgeeks is for geeks"
str2 = "geeks"

# using find() to find first occurance of str2
# returns 8
print("The first occurance of str2 is at : %d " % (str.find( str2, 4 )))

# using rfind() to find last occurance of str2
# returns 21
print("The last occurance of str2 is at : %d" % (str.rfind( str2, 4)))
