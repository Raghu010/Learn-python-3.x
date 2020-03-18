#eval function in python.

#It is a interesting utility in which a python code is run within the python program.
#The eval() method parses the expression passed to it and runs python code within the program.

"""The syntax of eval(expression, globals = None, locals = None)
expression: A string of statement which is parsed and evaluated.
globals(optional): a dictionary to specify global methods and variables.
locals(optional): a dictionary to specify local methods and variables."""

from math import *
def secret_function():
    return 'secret key is 1234'
def fn():
    expr = input('Expression in terms of x:')
    x = int(input('The value of x is:'))
    y = eval(expr)
    print('y = {}'.format(y))
fn()

"""Let us analyze the code a bit:

The above function takes any expression in variable x as input.
Then user has to enter a value of x.
Finally, we evaluate the python expression using eval() built-in function by passing the expr as argument.

Vulnerability issues with python.
The user can expose any hidden values in the program, or call dangerous function as eval will execute anything passed to it.

Consider the situation when you have imported os module in your program. This module provides the portable way to use operating functionalities like: read and write
A single command can delete all the files in your system."""

#Making eval safe:
#eval function comes with the facility of explicitly passing a list of variables and functions that it can access. We need to pass it as argument in the form of dictionary.

from math import *
def secret_function():
    return 'Secret key is 1234'
def fn():
    expr = input('Expression in terms of x:' )
    x = int(input('enter the value of x:'))
    safe_dict['x'] = x
    y = eval(expr, {'__builtins__':None}, safe_dict)
    print('y = {}'.format(y))
safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 
                 'tan', 'tanh']
safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
fn()

"""Now if we try to run above program like:

Enter the function(in terms of x):secret_function()
Enter the value of x:0
We get output:

NameError: name 'secret_function' is not defined
Let us analyze above code step by step:

First of all, we create a list of methods we want to allow as safe_list.
Next, we create a dictionary of safe methods. In this dictionary, keys are the method names and values are their local namespaces.
safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
locals() is a built-in method which returns a dictionary which maps all the methods and variables in local scope with their namespaces.

safe_dict['x'] = x
Here, we add local variable x to the safe_dict too. No local variable other than x will get identified by eval function.

eval accepts dictionaries of local as well as global variables as arguments. So, in order to ensure that none of the built-in methods is available to eval expression, we pass another dictionary along with safe_dict as well, as shown below:
y = eval(expr, {"__builtins__":None}, safe_dict)
So, in this way, we have made our eval function safe from any possible hacks!"""
