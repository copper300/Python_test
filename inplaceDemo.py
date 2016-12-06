# Python code to demonstrate the working of
# iadd() and iconcat()

import operator

# using iadd() to add and assign value
x = operator.iadd(2, 3)

# printing the modified value
print("The value after adding and assigning : ")
print(x)

# initializing value
y = "geeks"
z = "forgeeks"

# using iconcat() to concat the sequences
y = operator.iconcat(y,z)

print("The string after concatenation is : ")
print(y)

# Python code to demonstrate the working of
# isub() and imul()

# using isub() to subtract and assign value
x = operator.isub(2, 3)

print("The value after subtracting and assigning : ")
print(x)

# using imul() to multiply and assign value
x = operator.imul(2, 3)

print("The value after multiplying and assigning : ")
print(x)

# Python code to demonstrate the working of
# itruediv() and imod()

# using itruediv() to divide and assign value
x = operator.itruediv(10, 5)

print("The value after dividing and assigning : ")
print(x)

# using imod() to modulus and assign value
x = operator.imod(10, 6)

print("The value after modulus and assigning : ")
print(x)

# Python code to demonstrate the working of
# ixor() and ipow()

# using ixor() to exclusive or and assign value
x = operator.ixor(10, 5)

print("The value after xoring and assigning : ")
print(x)

# using ipow() to exponentiate and assign value
x = operator.ipow(5,4)
print("The value after exponentiating and assigning : ")
print(x)

# Python code to demonstrate the working of
# ior() and iand()

# using ior() to or, and assign value
x = operator.ior(10,5)
print("The value after bitwise or and assigning : ")
print(x)

# using iand() to and , and assign value
x = operator.iand(5,4)
print("The value after bitwise and, and assigning : ")
print(x)

# Python code to demonstrate the working of
# ilshift() and irshift()

# using ilshift() to bitwise left shift and assign value
x = operator.ilshift(8, 2)
print("The value after bitwise left shift and assigning : ")
print(x)

# using irshift() to bitwise right  shift and assign value
x = operator.irshift(8, 2)
print("The value after bitwise right shift and assigning : ")
print(x)
