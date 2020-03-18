def add(x, y):
    return x+y
def sub(x, y):
    return x-y



#from import statement: Python’s from statement lets you import specific attributes from a module.

#example for using from keyword while importing a particular attribute.

from math import sqrt, factorial
print(sqrt(16))
print(factorial(5))

#Note: If you only use import statement then the following command should be executed.

import math
print(math.sqrt(16))
print(math.factorial(5))

import random
print(dir(math))

#code snippet illustrating python built-in modules.
import math
print(math.sqrt(25))
print(math.pi)
print(math.degrees(2))
print(math.radians(60))
print(math.sin(2))
print(math.cos(0.5))
print(math.tan(.23))
print(math.factorial(3))

#importing built-in module random.
import random
print(random.randint(0, 5))
print(random.random())
print(random.random()*100)

L = [1, 2.1, True, 'Hi', 1+2j]
print(random.choice(L))

#importing built-in module datetime.
import datetime
from datetime import date
import time
print(time.time()) #returns the number of seconds from unix Epoch, January 1st 1970.
print(date.fromtimestamp(454554))
