#Random Module in python.

"""Python defines a set of functions to generate or manipulate random numbers. This particular type of functions are required in games, lotteries or any application
requiring the random number generation"""

#1.choice()- This function is required to generate the random number from a container.

import random
a = [1, 2, 3 , 4, 5]
print(random.choice(a))

"""2.randrange()- This function is used to generate a random number but within the range specified in the argument. This function takes 3 arguments, beginning
number (included in generation), last number (excluded in generation) and step ( to skip numbers in range while selecting)."""

import random
print(random.randrange(20, 50, 3))

#3.random()- This function is used to generate a random floating number greater than 1 and less than 0.
import random
print(random.random())

#4.seed()- This function maps a particular random number with the seed argument mentioned as the argument.
import random
random.seed(5)
print(random.random())
random.seed(7)
print(random.random())
random.seed(5)
print(random.random())
random.seed(7)
print(random.random())

#5.shuffle()- This function is used to shuffle the entire list to randomly arrange them.
import random
li = [1, 2, 3, 4, 5]
for i in range(0, len(li)): 
    print (li[i], end=" ") 
random.shuffle(li)
for i in range(0, len(li)):
    print(li[i], end = '\n')

"""6.uniform(a, b)- This function is used to generate a random floating point number between a range specified inside the paranthesis. It takes two arguments, lower
limit(included in generation) and upper limit(not included in generation)."""
import random
print(random.uniform(10, 15))
    
