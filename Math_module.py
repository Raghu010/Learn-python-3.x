#Examples for few mathematical functions present in math module.

#1.ceil()- Returns the greater digit then the entered value.
import math
print(math.ceil(4.5))
print(math.ceil(-3.4))

#2.floor()- Returns the lesser digit then the entered value.
print(math.floor(3.4))
print(math.floor(-2.1))

#3.fabs()- Returns the absolute value of an integer.
print(math.fabs(-10))
print(math.fabs(10))

#4.factorial()- Returns the factorial of a passed parameter.
print(math.factorial(6))
print(math.factorial(0))
#print(math.factorial(-2))

#5.gcd()- This function returns highest common factor of 2 passed parameters as output.
print(math.gcd(5, 15))

#6.copysign()- Takes 2 parameters and return the value of 1st parameter and the sign of second parameter.
print(math.copysign(5, -10))

#7.exp(a)- This function returns the exponent of passed parameter.
print(math.exp(1))

#8.log(a, b)- This function return the log value of 'a' w.r.t the base 'b'.
print(math.log(3, 2))

#9.log2(a)- This function returns log value of 'a' with base 2. This function returns the accurate value then the function discussed above.
print(math.log2(3))

#10.log10(a)- This function returns the log of 'a' with base 10. This function returns the accurate value then the function discussed above.
print(math.log10(2))


#11.pow(a, b)- This function return a raised to b.
print(math.pow(2, 2))

#12.sqrt()- This function returns the sqrt of a passed parameter.
print(math.sqrt(25))

#13.sin()- This function returns the sin of passed parameter. The value passed as a parameter should be in Radians
print(math.sin(1))

#14.cos()- This function returns the cos of passed parameter. The value passed as a parameter should be in Radians.
print(math.cos(1))

#15.tan()- This function returns the tangent of passed parameter. The value passed as a parameter should be in Radians.
print(math.tan(1))

#16.hypot(a, b) - This function returns the hypotenus of values passed.
print(math.hypot(3, 4))

#17.degrees()- This function is used to convert argument passed from radians to degrees.
a = math.pi/6
print(math.degrees(a))

#18.Radians()- This function is used to convert argument passed from degrees to radians.
b = 30
print(math.radians(b))

#19.gamma()
import math
a = 4
print(math.gamma(a))

#20.pi- This is the inbuilt constant which outputs value of 'pi'.
print(math.pi)

#21.e- This is the inbuilt constant which outputs value of 'e'.
print(math.e)

#22.inf- This is the inbuilt constant which outputs value of positive infinity.
print(math.inf)

#23.isinf()- This function is used to check whether the entered number is infinity or not.
if(math.isinf(math.inf)):
    print('Positive Infinity')
else:
    print('Not Infinity')

#24.nan- Not a number
print(math.nan)

#25.isnan()- Is used to verify nan value.
if(math.isnan(math.nan)):
    print('NAN')
else:
    print('not NAN')
