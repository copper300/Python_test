# Python programs to demonstrate list comprehension in Python
# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 12) if x % 2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x**2)
print(odd_square)

# below list contains power 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print(power_of_2)

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

# list for lowering the characters
print([x.lower() for x in ["A", "B", "C"]])

# list which extracts number
string = "my phone number is : 11122 !!"
print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print(numbers)

# A list of list for multiplication table
a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print("\nMultiplication Table")
for i in table:
    print(i)

# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst = range(1, 11)
print(lst)

# below list has numbers from 2 to 5
lst1_5 = lst[1 : 5]
print(lst1_5)

# below list has numbers from 6 to 8
lst5_8 = lst[5 : 8]
print(lst5_8)

# below list has number from 2 to 10
lst1_ = lst[1 : ]
print(lst1_)

# below list has numbers from 1 to 5
lst_5 = lst[ : 5]
print(lst_5)

# below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1 : 8 : 2]
print(lst1_8_2)

# below list has numbers from 10 to 1
lst_rev = lst[ : : -1]
print(lst_rev)

# below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9 : 4 : -2]
print(lst_rev_9_5_2)

# filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print(lst)

# filtering odd square which are divisble by 5
lst = filter(lambda x : x % 5 == 0, [x ** 2 for x in range(1, 11) if x % 2 == 1])
print(lst)

# filtering negative number
lst = filter(lambda x : x < 0, range(-5, 5))
print(lst)

# implementing max() function, using
print reduce(lambda a,b : a if (a > b) else b, [7, 12, 45, 100, 15])

# Python code to demonstrate the working of
# "in" and "not in"
# initializing list
lis = [1, 4, 3, 2, 5]

# checking if 4 is in list using "in"
if 4 in lis:
    print("List is having element with value 4")
else:
    print("List is not having element with value 4")

# checking if 4 is not list using "not in"
if 4 not in lis:
    print("List is not having element with value 4")
else:
    print("List is having element with value 4")

# Python code to demonstrate the working of
# len(), min() and max()
# initializing list 1
lis = [2, 1, 3, 5, 4]

# using len() to print length of list
print("The length of lis is : %d" % (len(lis)))

# using min() to print minimum element of list
print("The minimum element of list is : %d" % (min(lis)))

# using max() to print maximum element of list
print("The maximum element of list is : %d" % (max(lis)))

# Python code to demonstrate the working of
# "+" and "*"
# initializing list 1
lis = [1, 2, 3]

# initializing list 2
lis1 = [4, 5, 6]

# using "+" to concatenate lists
lis2 = lis + lis1

# printing concatenated lists
print("list after concatenation is :")
for i in range(0, len(lis2)):
    print(lis2[i])
print("\r")

# using "*" to combine lists
lis3 = lis * 3

# printing combined lists
print("list after combining is :")
for i in range(0, len(lis3)):
    print(lis3[i])
# Python code to demonstrate the working of
# del and pop()

# initializing list
lis = [2, 1, 3, 5, 4, 3, 8]

# using del to delete elements from pos 2 to 5
# delete 3, 5,4
del lis[2 : 5]

# displaying list after deleting
print("List elements after deleting are :")
for i in range(0, len(lis)):
    print(lis[i])
print("\r")

# using pop to delete element at pos 2
# delete 3
lis.pop(2)

# displaying list after popping
print("List elements after popping are :")
for i in range(0, len(lis)):
    print(lis[i])

# python code to demonstrate the working of
# insert() and remove()

# initailzing list
lis = [2, 1, 3, 5, 3, 8]

# using insert() to insert 4 at 3rd pos
lis.insert(3, 4)

# displaying list after inserting
print("List elements after inserting 4 are : ")
for i in range(0, len(lis)):
    print(lis[i])
print("\r")

# using remove() to remove first occurrence of 3
# remove 3 at pos 2
lis.remove(3)

# displaying list after removing
print("List elements after removing are :")
for i in range(0, len(lis)):
    print(lis[i])

# Python code to demonstrate the working of
# sort() and reverse()

# initializing list
lis = [2, 1, 3, 5, 3, 8]
# using sort() to sort the list\
lis.sort()
# displaying list after sorting
print("List elements after sorting are: ")
for i in range(0, len(lis)):
    print(lis[i])

# using reverse() to reverse the list
lis.reverse()
# displaying list after reversing
print("List elements after reversing are :")
for i in range(0, len(lis)):
    print(lis[i])

# Python code to demonstrate the working of
# extend() and clear()

# initializing list 1
lis1 = [2, 1, 3, 5]
# initializing list 2
lis2 = [6, 4, 3]
# using extend() to add elements of lis2 in lis1
lis1.extend(lis2)
# displaying list after sorting
print("List elements after extending are:")
for i in range(0, len(lis1)):
    print(lis1[i])
print("\r")

# using clear() to delete all lis1 elements
# lis1.clear()

# displaying list after clearing
print("List elements after clearing are :")
for i in range(0, len(lis1)):
    print(lis1[i])

