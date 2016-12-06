# python code to demonstrate the working of
# ceil() and floor()

# import "math" for math
import math
a = 2.3

# returning the ceil of 2.3
print("The ceil of 2.3 is : ")
print(math.ceil(a))

# returning the floor of 2.3
print ("The floor of 2.3 is : ")
print(math.floor(a))

# Python code to demonstrate the working of
# fabs() and factorial()
a = -10
b = 5
# Returning the absolute value.
print("The absolute value of -10 is : ")
print(math.fabs(a))

# returning the factorial of 5
print("The factorial of 5 is : ")
print(math.factorial(b))

# Python code to demonstrate the working of
# copysign() and gcd()

a = -10
b = 5.5
c = 15
d = 5

# returning the copysigned value
print("The copysigned value of -10 and 5.5 is : ")
print(math.copysign(5.5, -10))

# returning the gcd of 15 and 5
import fractions
print("The gcd of 5 and 15 is : ")
print(fractions.gcd(5, 15))

# Python code to demonstrate the working of
# exp() and log()

# returning the exp of 4
print("The e**4 value is : ")
print(math.exp(4))

# returning the log of 2,3
print("The value of log 2 with base 3 is : ")
print(math.log(2, 3))

# returning the log2 of 16
print("The value of log2 of 16 is : ")
print(math.log(16, 2))

# returning the log10 of 10000
print("The value of log10 of 10000 is : ")
print(math.log10(10000))

# Python code to demonstrate the working of
# pow() and sqrt()

# returning the value of 3**2
print("The value of 3 to the power 2 is : ")
print(math.pow(3, 2))

# returning the square root of 25
print("The value of square root of 25 : ")
print(math.sqrt(25))

# Python code to demonstrate the working of
# sin() and cos()

a = math.pi / 6

# returning the value of sine of pi/6
print("The value of sine of pi/6 is : ")
print(math.sin(a))

# returning the value of cosine of pi/6
print("The value of cosine of pi/6 is : ")
print(math.cos(a))

# Python code to demonstrate the working of
# tan() and hypot()
a = math.pi/6
b = 3
c = 4

# returning the value of tangent of pi/6
print("The value of tangent of pi/6 is : ")
print(math.tan(a))

# returning the value of hypotenuse of 3 and 4
print("The value of hypotenuse of 3 and 4 is : ")
print(math.hypot(b,c))

# Python code to demonstrate the working of
# degree() and radians()

a = math.pi/6
b = 30

# returning the converted value from radians to degrees
print("The converted value from radians to degree is : ")
print(math.degrees(a))

# returning the converted value from degrees to radians
print("The converted value from degrees to radians is : ")
print(math.radians(b))

# Python code to demonstrate the working of
# gamma()
a = 4
# returning the gamma() of 4
print("The gamma() of 4 is : ")
print(math.gamma(a))

# returning the value of constant pi
print("The value of constant pi is : ")
print(math.pi)

# returning the value of constant e
print("The value of constant e is : ")
print(math.e)

# checking the number is nan
b = float('inf')
a = float('nan')
if (math.isnan(a)):
    print("The number is nan")
else:
    print("The number is not nan")

# checking the number is positive infinity
if (math.isinf(b)):
    print("The number is positive infinity")
else:
    print("The number is not positive infinity")
