# Python code to demonstrate working of
# startwith() and endswith()
str = "geekforgeeks"
str1 = "geeks"

# using startwith() to find if str starts with str1
if str.startswith(str1):
    print("%s begins with %s" % (str, str1))
else:
    print("%s does not begin with %s" % (str, str1))

# using endswith() to find if str ends with str1
if str.endswith(str1):
    print("%s ends with %s" % (str, str1))
else:
    print("%s does not end with %s" % (str, str1))
