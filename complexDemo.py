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
