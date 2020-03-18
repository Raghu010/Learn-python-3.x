#urllib module in python.

"""Urllib module is the url handling module for python. It is used fetch URL's(uniform resource locators). It uses the urlopen() and is able to fetch url's using a
variety of different protocols"""

#Urllib is a package that collects several modules for working with URL's.

"""urllib.request for opening and reading.
urllib.parse for parsing the URL's.
urllib.error for raising the exception.
urllib.robotparser for parsing the robot.txt files."""

#1.urllib.request - This module helps to define functions and classes to open URLs.

import urllib.request
a = urllib.request.urlopen('https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python')
print(a.read())

"""2.urllib.parse - This module helps to define functions to manipulate URLs and their component parts, to make or brake them. It usually focus on breaking the
components into smaller parts or joining different URL parts to form a string."""

from urllib.parse import *
a = urlparse('https://www.hackerrank.com/ domains')
print(a)
b = urlunparse(a)
print(b)


"""3.urllib.error - This module defines the classes for exception raised by urllib.request. Whenever there is an error when fetching an URL This module helps in
raising exceptions.

URLError – It is raised for the errors in URLs, or errors while fetching the URL due to connectivity, and has a ‘reason’ property that tells a user the reason of
error.

HTTPError – It is raised for the exotic HTTP errors, such as the authentication request errors. It is a subclass or URLError. Typical errors include ‘404’ (page not found), ‘403’ (request forbidden),
and ‘401’ (authentication required)."""

import urllib.request
import urllib.parse
try:
    a = urllib.request.urlopen('https://www.google.com')
    print(a.read())
except Exception as e:
    print(e)

#example2.
import urllib.request
import urllib.parse
try:
    a = urllib.request.urlopen('https://www.google.com/ search?q = test')
except Exception as e:
    print(e)

"""urllib.robotparse- This module contains a single class Robotfileparser. This class answers question about whether or not, user can fetch a URL that publish
robot.txt files. Robots.txt is a text file webmasters create to instruct web robots how to crawl pages on their website. The robot.txt file tells the web
scraper about what parts of the server should not be accessed."""

# importing robot parser class 
import urllib.robotparser as rb 
  
bot = rb.RobotFileParser() 
  
# checks where the website's robot.txt file reside 
x = bot.set_url('https://www.geeksforgeeks.org / robot.txt') 
print(x) 
  
# reads the files 
y = bot.read() 
print(y) 
  
# we can crawl the main site 
z = bot.can_fetch('*', 'https://www.geeksforgeeks.org/') 
print(z) 
  
# but can not crawl the disallowed url 
w = bot.can_fetch('*', 'https://www.geeksforgeeks.org / wp-admin/') 
print(w)
