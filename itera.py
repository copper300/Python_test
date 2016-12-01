# Accessing items using for-in loop
cars = ["Aston", "Audi", "Mclaren"]
for x in cars:
    print(x)

# Accessing items using indexes and for-in
for i in range(len(cars)):
    print(cars[i])

# Accessing items using enumerate()
for i, x in enumerate(cars):
    print(x)

# Accessing items and indexes enumerate()
for x in enumerate(cars):
    print(x[0], x[1])

# Printing return value of enumerate
print(enumerate(cars))

# demonstrating use of start in enumerate
for x in enumerate(cars, start = 1):
    print(x[0], x[1])

# Two seperate lists
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and its accessories.
# First two items store prices of cars and next
# three items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$", 4:"890000$", 5:"4500$"}

# printing prices of cars
for index, c in enumerate(cars, start = 1):
    print("Car: %s Prices: %s" % (c, prices[index]))

# printing prices of accessories
for index, a in enumerate(accessories, start = 1):
    print("Accessory: %s Prices: %s" % (a, prices[index]))

# Python program to demonstrate unzip (reverse
# of zip)using * with zip function
l1, l2 = zip(*[('Aston', 'GPS'),('Audi', 'Car Repair'),('Mclaren', 'Dolby sound kit')])
# Printing unzipped lists
print(l1)
print(l2)
