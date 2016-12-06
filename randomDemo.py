# Python code to demonstrate the working of
# choice() and randrange()
import random

# using choice() to generate a random number from a
# given list of numbers.
print("A random number from list is : ")
print(random.choice([1, 4, 8, 10, 3]))

# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting
print("A random number from range is : ")
print(random.randrange(20, 50, 3))

# Python code to demonstrate the working of
# random() and seed()
# using random() to generate a random num
# between 0 and 1
print("A random number between 0 and 1 is : ")
print(random.random())

# using seed() to seed a random number
random.seed(5)

print("The mapped random number with 5 is : ")
print(random.random())

random.seed(7)
print("The mapped random number with 7 is : ")
print(random.random())

random.seed(5)
print("The mapped random number with 5 is : ")
print(random.random())

random.seed(7)
print("The mapped random number with 7 is : ")
print(random.random())

# Python code to demonstrate the working of
# shuffle() and uniform()
li = [1, 4, 5, 10, 2]
print("The list before shuffling is : ")
for i in range(0, len(li)):
    print(li[i])
print("\r")

# using shuffle() to shuffle the list
random.shuffle(li)

print("The list after shuffling is : ")
for i in range(0, len(li)):
    print(li[i])
print("\r")

# using uniform() to generate random floating number in range
print("The random floating point number between 5 and 10 is : ")
print(random.uniform(5, 10))

