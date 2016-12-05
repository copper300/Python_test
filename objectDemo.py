# A simple example class
class Test:
    # A sample method
    def fun(self):
        print("Hello")

# Driver code
obj = Test()
obj.fun()

# A Sample class with init method
class Person:
    # init method or constuctor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello, my name is %s" % self.name)
p = Person('Shwetanshu')
p.say_hi()

# Python program to show that the variable with a value
# assigned in class declaration, are class variable and
# variable inside methods and constuctors are instance
# variable

# Class for Compute Science Student
class CSStudent:
    # Class variable
    stream = 'cse'

    # The init method or constuctor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll
# Object of CSStudent class
a = CSStudent(101)
b = CSStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)

# Class variables can be accessed using class
# name also
print(CSStudent.stream)

# Python program to show that we can create
# instance variables inside methods
# Class for Computer Science Student
class CSStudent:
    # Class variable
    stream = 'cse'

    # The init method or constuctor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll

    # Adds an Instance variable
    def setAddress(self,address):
        self.address = address
    # Retrieves instance variable
    def getAddress(self):
        return self.address

# Driver code
a = CSStudent(101)
a.setAddress("Nodia, UP")
print(a.getAddress())

class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0
    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)
# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
# print(myObject.__hiddenVariable)

# A Python program to demonstrate that hidden
# members can be accessed outside a class
print(myObject._MyClass__hiddenVariable)

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
# Driver Code
t = Test(1234, 5678)
print(t)

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is employee
    def isEmployee(self):
        return False

    # Inherited or Sub Class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())

# Python exmple to check if a class is
# subclass of another
class Base(object):
    pass
class Derived(Base):
    pass

# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))

# Python example to show working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        # Calling constuctors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    def printStrs(self):
        print(self.str1, self.str2)
ob = Derived()
ob.printStrs()

# Python example to show that base
# class members can be accessed in
# derived class using base class name
class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x

class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(Base.x, self.y)

# Driver Code
d = Derived(10, 20)
d.printXY()

# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):
    def __init__(self, x):
        self.x = x

class Derived(Base):
    def __init__(self, x, y):
        super(Derived, self).__init__(x)
        self.y = y

    def printXY(self):
        print(self.x, self.y)

# Driver Code
d = Derived(10, 20)
d.printXY()

# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent(object):
    stream = 'cse'
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

print(CSStudent.stream)

print("Initially")
print("a.stream =", a.stream)
print("b.stream =", b.stream)

# This thing doesn't change class(static) variable
# Instead creates instance variable for the object
# 'a' that shadows class member.
a.stream = 'ece'

print("\nAfter changing a.stream")
print("a.stream =", a.stream)
print("b.stream =", b.stream)

# Program to show how to make changes to the
# class variable in Python

CSStudent.stream = "mec"
print("\nClass variable changes to mec")

print("\nValue of variable stream for each object")
print("a.stream =", a.stream)
print("b.stream =", b.stream)
