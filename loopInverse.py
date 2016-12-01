str = "geekforgeeks"
list1 = []
for i in range(1, len(str) + 1):
    list1.append(str[-i])

str1 = ''.join(list1)
print(str1)
