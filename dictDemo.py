# Python code to demonstrate working of
# str() and items()

# Initializing dictionary
dic = {"Name" : "Nandini", "Age": 19}

# using str() to display dic as string
print("The constituents of dictionary as string are :")
print(str(dic))

# using item() to display dic as list
print("The constituents of dictionary as list are : ")
print(dic.items())

# Python code to demonstrate working of
# len() and type()

# Initializing dictionary
dic = {"Name" : "Nandini", "Age" : 19, "ID" : 2541997}

# Initializing list
li = [1, 3, 5, 6]

# using len() to display dic size
print("The size of dic is : %d" % len(dic))

# using type() to display data type
print("The data type of dic is : %s" % type(dic))

# using type() to display data type
print("The data type of li is : %s" % type(li))

# Python code to demonstrate working of
# clear() and copy()

# Initializing dictionary
dic1 = {'Name' : 'Nandini', 'Age' : 19}

dic3 = {}

# using copy to make shallow copy of dictionary
dic3 = dic1.copy()

# printing the new dictionary
print("The new copied dictionary is : ")
print(dic3.items())

# clearing the dictionary
dic1.clear()

# printing the cleared dictionary
print("The contents of deleted dictionary is : ")
print(dic1.items())

# Python code to demonstrate working of
# fromkeys() and update()

# Initializing dictionary 1
dic1 = {'Name' : 'Nandini', 'Age' : 19}

dic2 = {'ID' : 2541997}

# Initializing sequence
sequ = ('Name', 'Age', 'ID')

# using update to add dict2 values in dic1
dic1.update(dic2)

# printing the updated dictionary values
print("The updated dictionary is : ")
print(str(dic1))

# using fromkeys() to transform sequence into dictionary
dict = dict.fromkeys(sequ, 5)

# printing the new dictionary values
print("The new dictionary values are : ")
print(str(dict))

# Python code to demonstrate working of
# has_key() and get()

dict = {"Name" : "Nandini", "Age" : 19}

# using has_key() to check if dic1 has a key
if dict.has_key('Name'):
    print("Name is a key")
else:
    print("Name is not a key")

# using get() to print a key value
print("The value associated with ID is")
print(dict.get('ID', "Not present"))

# printing dictionary values
print("The dictionary values are : ")
print(str(dict))

# Python code to demonstrate working of
# setdefault()

# Initializing dictionary

dict = {"Name" : "Nandini", "Age" : 19}

# using setdefault to print a key value
print("The value associated with ID is : ")
print(dict.setdefault('ID', "No ID"))

# printing dictionary values
print("The dictionary values are : ")
print(str(dict))
