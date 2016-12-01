# A sample program to demonstrate unpacking of
# dictionary items using **
def fun1(a, b, c):
    print(a, b, c)

# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun1(**d)


# A sample program to demostrate packing of
# dictionary items with **
def fun2(**kwargs):
    # kwargs is a dict
    print(type(kwargs))

    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

# Driver code
fun2(name='geeks', ID="101", language="Python")
