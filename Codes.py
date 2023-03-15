

name = "John Smith" #string
age = 30 #integer
height = 1.75 #float
is_student = True #boolean

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

for i in range(10):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

#List comprehension
squares = [x**2 for x in range(10)]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

def add_numbers(x, y): 
    return x + y 

result = add_numbers(5, 10)
print(result) #15

import math
x = math.sqrt(16)
print(x) #4.0

class Dog: 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age 

  def bark(self): 
    print("Woof!") 

my_dog = Dog("Fido", 3) 
print(my_dog.name) #Fido 
print(my_dog.age) #3
my_dog.bark() #Woof!

#Writing to a file
with open("example.txt", "w") as file: 
  file.write("This is an example file.")

#Reading from a file
with open("example.txt", "r") as file: 
  contents = file.read() 
  print(contents) #This is an example file.

try: 
    x = 5 / 0 
except ZeroDivisionError: 
    print("Cannot divide by zero.") 

#This code will attempt to divide 5 by 0. If the division is successful, the code will continue, however since division by zero is not possible, the code will throw a ZeroDivisionError. The except block will catch the error and print "Cannot divide by zero" to the console.

import re 
text = "The phone number is 555-555-5555." 
phone_number = re.search(r"\d{3}-\d{3}-\d{4}", text) 
print(phone_number.group()) #555-555-5555

#This line of code will import the regular expression library and then search for a pattern of three digits, followed by a hyphen, followed by three digits, followed by a hyphen, followed by four digits within the string "The phone number is 555-555-5555.". The result is that the phone number 555-555-5555 will be printed to the console.


from bs4 import BeautifulSoup #imports the Beautiful Soup library
import requests #imports the requests library
url = "https://www.example.com" #stores the url in a variable
page = requests.get(url) #requests the web page from the url
soup = BeautifulSoup(page.content, "html.parser") #creates a Beautiful Soup object from the web page
print(soup.prettify()) #prints the web page in a formatted manner

#This line of code will import the Beautiful Soup and Requests libraries, store a url in a variable, request the web page from the url, create a Beautiful Soup object from the web page, and then print the web page in a formatted manner.

import pandas as pd #import pandas library
import numpy as np #import numpy library
import matplotlib.pyplot as plt #import matplotlib library

#using pandas to read a csv file
df = pd.read_csv("data.csv") #read in data.csv file
print(df.head()) #print the first five rows of the data

#using numpy to perform mathematical operations
a = np.array([1, 2, 3, 4, 5]) #create an array of numbers
b = np.array([5, 4, 3, 2, 1]) #create second array of numbers
c = a + b #add the two arrays together
print(c) #print the result of the addition

#using matplotlib to create a bar chart
data = {'apples': 10, 'oranges': 15, 'lemons': 5
