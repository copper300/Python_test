# Python code to demonstrate the working of
# array(), append(), insert()

# importing "array" for array operation
import array

# Initializing array with array values
# Initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print("The new create array is:")
for i in range(0,3):
    print(arr[i])
print("\r")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr.insert(2, 5)

# printing array after insertion
print("The array after insertion is :")
for i in range(0, 4):
    print(arr[i])
print("\r")

# using append() to insert new value at end
arr.append(4)
# printing appended array
print("The appended array is : ")
for i in range(0, 5):
    print(arr[i])

# Python code to demonstrate the working of
# pop() and remove()

# initializing array with array values
arr = array.array('i', [1, 2, 3, 1, 5])
for i in range(0, 5):
    print(arr[i])

# using pop() to remove element at 2nd position
print("The popped element is : ")
print(arr.pop(2))

# printing array after popping
print("The array after popping is : ")
for i in range(0,4):
    print(arr[i])

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print("The array after removing is : ")
for i in range(0,3):
    print(arr[i])

# Python code to demonstrate the working of
# index() and reverse()

# initializing array with array values
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing the original array
print("The new created array is : ")
for i in range(0,6):
    print(arr[i])

# using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ")
print(arr.index(2))

# using reverse() to reverse the array
arr.reverse()

# printing array after reversing
print("The array after reversing is ")
for i in range(0, 6):
    print(arr[i])

# Python code to demonstrate the working of typecode
# itemsize, buffer_info()
# initializing array with array values
arr = array.array('i',[1, 2, 3, 1, 2, 5])

# using typecode to print datatype of array
print("The datatype of array is : ")
print(arr.typecode)

# using itemsize to print itemsize of array
print("The itemsize of array is : ")
print(arr.itemsize)

# using buffer_info() to print buffer info of array
print("The buffer info of array is : ")
print(arr.buffer_info())

# Python code to demonstrate the working of
# count() and extend()

# initializing array 1 with array values
arr1 = array.array('i', [1, 2, 3, 1, 2, 5])

# initializing array 2 with array values
arr2 = array.array('i', [1, 2, 3])

# using count() to count occurrence of 1 in array
print("The occurrence of 1 in array is : ")
print(arr1.count(1))

# using extend() to add array 2 elements to array 1
arr1.extend(arr2)

print("The modified array is : ")
for i in range(0,9):
    print(arr1[i])

# Python code to demonstrate the working of
# fromlist() and tolist()

# initializing array with array values
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)

# printing the modified array
print("The modified array is : ")
for i in range(0,9):
    print(arr[i])

# using tolist() to convert array to list
li2 = arr.tolist()
print("\r")

# printing the new list
print("The new list created is : ")
print(li2)
