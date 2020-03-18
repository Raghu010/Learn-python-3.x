#Fraction Module in python.
#This module provides support for rational number arithmetic. It allows to create fraction instance from integers, float, string and decimal values.
#Fraction instances are created from two integers, from another rational number or from a string. Fraction instances are hashable thus are immutable.


"""1.class fractions.Fraction(numerator=0, denominator=1) : This requires that numerator and denominator are instances of numbers. Rational and a fraction instance
with value = (numerator/denominator) is returned. A zerodivision error is raised if denominator = 0."""

from fractions import Fraction
print(Fraction(11, 35))
print(Fraction(10, 18))
print(Fraction())

"""2.class fractions.Fraction(other_fraction) : This requires that other_fraction is instance of numbers.Rational and a fraction instance with same value is returned"""

from fractions import Fraction
print(Fraction(3.141592653589793238))
print(Fraction(3.141592653589793238))


"""3.class fractions.Fraction(decimal): This function requires a decimal instance and the equivalent fractional instance is returned as an output."""

from fractions import Fraction
print(Fraction('1.13'))

"""4.class fractions.Fraction(string): This function requires string or unicode instance and the equivalent fractional instance is obtained as an output."""

from fractions import Fraction
print(Fraction('5/11'))
print(Fraction('1.13'))
print(Fraction('1.414213'))

"""5.limit_denominator(max_denominator=1000000) :
This method is useful for finding rational approximations to a given floating-point number.
This module finds and returns the closest Fraction to self that has denominator at most max_denominator.
This module can also be used to return the numerator of a given fraction in the lowest term by using the numerator property and the denominator by using the
denominator property."""

from fractions import Fraction
print(Fraction('3.14159265358979323846'))
print(Fraction('3.14159265358979323846').limit_denominator(10000))  
print(Fraction('3.14159265358979323846').limit_denominator(1000))   
print(Fraction('3.14159265358979323846').limit_denominator(100))
print(Fraction('3.14159265358979323846').limit_denominator(10))
print(Fraction(125, 50).numerator)
print(Fraction(125, 50).denominator)

#Performing mathematical operations on fractions.
from fractions import Fraction
print(Fraction(113, 100) + Fraction(25, 100))
print(Fraction(18, 5) / Fraction(18, 10))
print(Fraction(1, 2) * Fraction(2, 1))
print(Fraction(1, 2) ** Fraction(2, 1))

#Fraction-based calculations using various functions of math module.


import math
from fractions import Fraction
print(math.sqrt(Fraction(16, 4)))
print(math.sqrt(Fraction(82, 9)))
print(math.floor(Fraction(82, 9)))

print(Fraction(math.sin(math.pi/3)))
print(Fraction(math.sin(math.pi/3)).limit_denominator(10))
