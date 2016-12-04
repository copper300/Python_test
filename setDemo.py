#Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b", "c"}
normal_set = set(["a", "b", "c"])

# Adding an element to normal set is fine
normal_set.add("d")

print("Normal set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("Frozen Set")
print(frozen_set)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")

# Python programs to demonstrate working of
# Set in python

# Create two sets
set1 = set()
set2 = set()

# Adding elements to set1
for i in range(1, 6):
    set1.add(i)

# Adding element to set2
for i in range(3, 8):
    set2.add(i)

print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")

# Union of set1 and set2
set3 = set1 | set2
print("Union of set1 and set2 : set3 = ", set3)

# Intersection of set1 and set2
set4 = set1 & set2
print("Intersection of set1 and set2 : set4 = ", set4)
print("\n")

# Checking relation between set3 and set4
if set3 > set4: # set3.issuperset(set4)
    print("set3 is superset of set4")
elif set3 < set4:
    print("Set3 is subset of set4")
else:
    print("Set3 is same as set4")

# displaying relation between set4 and set3
set5 = set3 - set4
print("Elemnets in Set3 and not in Set4: Set5 = ", set5)
print("\n")
if set4.isdisjoint(set5):
    print("Set4 and Set5 have nothing in common \n")

# Removing all elements of set5
set5.clear()
print("After applying clear on sets Set5: ")
print("Set5 = ", set5)

