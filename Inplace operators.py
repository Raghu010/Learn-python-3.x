#Inplace operators in Python.

'''Python in it's definition provides some inplace operators, These operators will assign as well as compute in a single line'''
#for example x -= y is equivalent to operator.isub(x, y)
#Note: Inplace operators are defined in operator module.

#Below are some examples for performing inplace operations.

"""1.iadd()- This function is used to assign and add the current value. This operation does “a+=b” operation. Assigning is not performed in case of immutable containers,
such as strings, numbers and tuples."""

import operator
a = 5
b = 3
print(operator.iadd(a, b))

"""2.iconcat()- This function is used to concat first string at the end of second"""

a = 'Virat'
b = 'Kohli'
print(operator.iconcat(a, b))

"""3. isub() :- This function is used to assign and subtract the current value. This operation does “a-=b” operation. Assigning is not performed in case of immutable
containers, such as strings, numbers and tuples."""

a = 19
b = 7
print(operator.isub(a, b))

"""4.imul() :- This function is used to assign and multiply the current value. This operation does “a*=b” operation. Assigning is not performed in case of immutable
containers, such as strings, numbers and tuples."""

a = 16
b = 6
print(operator.imul(a, b))

"""5.itruediv() :- This function is used to assign and divide the current value. This operation does “a/=b” operation. Assigning is not performed in case of immutable
containers, such as strings, numbers and tuples."""

a = 64
b = 8
print(operator.itruediv(a, b))

"""6.imod()- This function is used to assign and return remainder. This operation does “a%=b” operation. Assigning is not performed in case of immutable containers,
such as strings, numbers and tuples."""

a = 3
b = 2
print(operator.imod(a, b))

"""7. ixor() :- This function is used to assign and xor the current value. This operation does “a^ = b” operation. Assigning is not performed in case of immutable
containers, such as strings, numbers and tuples."""

a = 1
b = 0
print(operator.ixor(a, b))

"""8.ipow() :- This function is used to assign and exponentiate the current value. This operation does “a ** = b” operation. Assigning is not performed in case of
immutable containers, such as strings, numbers and tuples."""

a = 3
b = 2
print(operator.ipow(a, b))

"""9.iand() :- This function is used to assign and bitwise and the current value. This operation does “a &= b” operation. Assigning is not performed in case of
immutable containers, such as strings, numbers and tuples"""

a = 1
b = 1
print(operator.iand(a, b))

"""10.ior()-  This function is used to assign and bitwise or the current value. This operation does “a |=b ” operation. Assigning is not performed in case of
immutable containers, such as strings, numbers and tuples."""
a = 5
b = 1
print(operator.ior(a, b))

"""11.ilshift()-This function is used to assign and bitwise leftshift the current value by second argument. This operation does “a <<=b ” operation. Assigning is not
performed in case of immutable containers, such as strings, numbers and tuples."""

a = 3
b = 2
print(operator.ilshift(a, b))

"""12.irshift()- This function is used to assign and bitwise rightshift the current value by second argument. This operation does “a >>=b ” operation. Assigning is not
performed in case of immutable containers, such as strings, numbers and tuples."""

a = 4
b = 1
print(operator.irshift(a, b))
