# python code to demonstrate the working of
# complex(), real() and imag()

import cmath

x = 5
y = 3

# converting x and y into complex number
z = complex(x,y)

# printing real and imaging part of complex number
print("The real part of complex number is : ")
print(z.real)

print("The imaginary part of complex number is : ")
print(z.imag)

# Python code to demonstrate the working of
# phase()

x = -1.0
y = 0.0

z = complex(x, y)

print("The phase of complex number is : ")
print(cmath.phase(z))

# Python code to demonstrate the working of
# polar() and rect()

x = 1.0
y = 1.0

z = complex(x, y)

# converting complex number into polar using polar()
w = cmath.polar(z)

print("The modulus and argument of polar complex number is : ")
print(w)

# converting complex number into rectangular using rect()
w = cmath.rect(1.4142135623730951, 0.7853981633974483)
print("The rectangular form of complex number is : ")
print(w)

# Python code to demonstrate the working of
# exp(), log()
x = 1.0
y = 1.0

# converting x and y into complex number
z = complex(x, y)

print("The exponent of complex number is : ")
print(cmath.exp(z))

print("The log(base 10) of complex number is : ")
print(cmath.log(z,10))

print("The log10 of complex number is : ")
print(cmath.log10(z))

print("The square root of complex number is : ")
print(cmath.sqrt(z))

# Python code to demonstrate the working of
# sin(), cos() and tan()

print("The sine value of complex number is : ")
print(cmath.sin(z))

print("The cosine value of complex number is : ")
print(cmath.cos(z))

print("The tangent value of complex number is : ")
print(cmath.tan(z))

print("The arc sine value of complex number is : ")
print(cmath.asin(z))

print("The arc cosine value of complex number is : ")
print(cmath.acos(z))

print("The arc tangent value of complex number is : ")
print(cmath.atan(z))

print("The hyperbolic sine value of complex number is : ")
print(cmath.sinh(z))

print("The hyperbolic cosine value of complex number is : ")
print(cmath.cosh(z))

print("The hyperbolic tangent value of complex number is : ")
print(cmath.tanh(z))

print("The inverse hyperbolic sine value of complex number is : ")
print(cmath.asinh(z))

print("The inverse hyperbolic cosine value of complex number is : ")
print(cmath.acosh(z))

print("The inverse hyperbolic tangent value of complex number is : ")
print(cmath.atanh(z))
