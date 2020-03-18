#Complex Module in Python.

"""Not only real numbers, Python can also handle complex numbers and its associated functions using the file “cmath”. Complex numbers have their uses in many
applications related to mathematics and python provides useful tools to handle and manipulate them."""

"""Converting real number to complex number:
A complex number is represented by “ x + yi “. Python converts the real numbers x and y into complex using the function complex(x,y). The real part can be accessed
using the function real() and imaginary part can be represented by imag()."""

import cmath
a = 1
b = 2
c = complex(a, b)
print(c)
print(c.real)
print(c.imag)

"""Phase of a complex number:
Geometrically, the phase of a complex number is the angle between the positive real axis and the vector representing complex number. This is also known as argument of
complex number. Phase is returned using phase(), which takes complex number as argument. The range of phase lies from -pi to +pi. i.e from -3.14 to +3.14."""

a = 3
b = 2
c = complex(a, b)
print(cmath.phase(c))

"""Converting from polar to rectangular form and vice-versa:
Conversion to polar is done using polar(), which returns a pair(r,ph) denoting the modulus r and phase angle ph. modulus can be displayed using abs() and phase using
phase().A complex number converts into rectangular coordinates by using rect(r, ph), where r is modulus and ph is phase angle. It returns a value numerically equal to
r * (math.cos(ph) + math.sin(ph)*1j)"""

import cmath
a = 1
b = 1
c = complex(a, b)
print(cmath.polar(c))
print(cmath.rect(1.4142135623730951, 0.7853981633974483))

#Few important functions and constants in python.

#1.exp(a)- This function returns the exponential of specified argument.
import cmath
a = 1
b = 1
c = complex(a, b)
print(cmath.exp(c))

#2.log(c, b)- This function returns the logarithamic value of 'c' with base 'b'
a = 3
b = 2
c = complex(a, b)
print(cmath.log(c, 10))

#3.log10()- This function returns log base 10 of a complex number.
print(cmath.log10(c))

#4.sqrt()-This function returns the square root of a complex number.
import cmath
a = 1.0
b = 1.0
c = complex(a, b)
print(cmath.sqrt(c))

#5.isfinite()- Returns true if both real and imaginary part of complex number are finite, else returns false.

x = 1.0
y = 1.0
z = complex(x, y)
if(cmath.isfinite(z)):
    print('True')
else:
    print('False')

#6.isinf()- Returns True if either of real or complex part is infinite.
import math
x = 1.0
y = math.inf
a = complex(x, y)
if(cmath.isinf(a)):
    print('True')
else:
    print('False')

#7.isnan()- Returns True if either of real or complex number is nan.
a = 1
b = math.nan
c = complex(a, b)
if(cmath.isnan(c)):
    print('True')
else:
    print('False')

"""Constants:
There are two constants defined in cmath module, “pi”, which returns the numerical value of pi. The second one is “e” which returns the numerical value of exponent."""

import cmath
print(cmath.pi)
print(cmath.e)


#Trigonometric and Hyperbolic functions.
#1.sin()-This function returns the sin of complex number passed as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.sin(z))

#2.cos()-This function returns the cos of complex number passed as a argument.
import cmath
x = 2.0
y = 1.0
z = complex(x, y)
print(cmath.cos(z))

#3.tan()- This function returns the tan of complex number passed as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.tan(z))

#Inverse Trigonometric functions.
#1.asin()- This function returns the arc sine of the complex number passed in as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.asin(z))

#2.acos()- This function returns the arc cosine of complex number passed in as a argument.
import cmath
x = 2.0
y = 1.0
z = complex(x, y)
print(cmath.acos(z))

#3.atan()- This function returns the arc tangent of a complex number passed in as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.atan(z))

#Hyperbolic functions:
#1.sinh()- This function returns the hyperbolic sine of a complex number passed in as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.sinh(z))

#2.cosh()- This function returns the hyperbolic cosine of a complex number passed in as a argumnet.
import cmath
x = 1.0
y = 2.0
z = complex(x, y)
print(cmath.cosh(z))

#3.tanh()- This function returns the hyperbolic tangent of a complex number passed as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.tanh(z))

#Inverse Hyperbolic functions:
#1.asinh()- This function returns the inverse hyperbolic sin of complex number passed as a argument.
import cmath
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.asinh(z))

#2.acosh()- This function returns the inverse cosine hyperbolic of passed complex argument.
import cmath
x = 2.0
y = 1.0
z = complex(x, y)
print(cmath.acosh(z))

#3.atanh()- This function return the inverse hyperbolic tangent of passed complex argument.
x = 1.0
y = 1.0
z = complex(x, y)
print(cmath.atanh(z))
