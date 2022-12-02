greeting ="hi, good afternoon"
print(greeting)
message = "buhari has done well in the easthern part of this nation"
print(message)
precious ="python is cool"
print(precious)



ball = ["red","green","yellow"]
precious, sam,joe = ball
print (precious)
print (sam)
print(sam)
if 5 > 2:
    print (" five is greater than TWO")
x = 6
y = "hello"
print(x)
print(y)
precious = "python is cool"
#precious ="python is cool"
"""" this is just a comment written in line"""
print(precious)
x = 8 
y = "joe"
print(x)
print(y)
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
x = "joe" # is the same as 
x = 'joe'
print (x)
x, y, z = "orange", "black", "green"
print(x)
print(y)
print(z)
x= y= z = "orange"
print(x)
print(y)
print(z)
x = "beautiful"
print("python is "+ x)
x = "python is "
y = "beautiful"
z = x + y
print(z)
x = 54
y = 2
print(x + y)
x = 3
y = "john"
print(x + y)
x = "beautiful"
def myfunc():
    print("python is " + x)
myfunc()
x = "beautiful"
def myfunc():
    x = "fantastics"
    print("python is " + x)
myfunc()
print("python is " + x)
x = "beautiful"
def myfunc():
    global x
    x = "fantastics"
myfunc()
print("python is " + x)
x = "john"
print (type(x))
x= 3 #int
y = 2.0 #floot
z = 5j #complex
print (type(x))
print (type(y))
print (type(z))
import random
print(random. randrange (2,11))
x = int(3) # it will be 3
y = int(3.0) # it will be 3
z = int("5") # it will be 5
print (x)
print (y)
print (z)
message = """ the boy started a business and endup crashing, the system is functioning well. """
print (message)
message =  '''the boy started a business and endup crashing, the system is functioning well. '''
print (message)
sam = "john"
print (sam[0c])
x = "brother"
print (len(x))
b = "grandfather"
print (b. replace ("g","m"))
g = "grand, mother"
print(g.split (","))
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
a = "world"
b = "Hello"
c = a + b
print (c)
age = 54
txt = "my name is john, i am" + age
print (txt)
a = 200
b = 30
if b > a:
    print ("b is greater than a")
else:
    print ("b is not greater than a")
printing an individual character
a = "piraTech"
print(a)
 
b = "pira" 
c = "Tech" 
# print(b)
b = "pira" 
c = "Tech"
print(c)

sam = "piratech"
print(sam.upper())
sam =  "piratech"
print(sam. lower())

sam = "piratech"
print(sam.replace ("pira","fus"))
a = "john"
b = "sam"
c = a +"  "+ b
print (c)
age = 34
txt = "my name is sam, and i am {}"
print (txt. format (age))
quanitity = 43
item = 37 
price = 54,6
myorder = "i went {} pieces of item {} for {} dollars"
print(myorder. format(quanitity, item, price))

company_name = "piratech"
for x in each company_name:
    print(x)
courses = ["maths", "english", "geography", "physics", "chemistry"]
courses. insert(6,"comp_sci")
print(courses)
courses = ["maths", "english", "geography", "physics", "chemistry"]
courses [1]= "economics"
print (courses)
courses = ["maths", "english", "geography", "physics", "chemistry"]
for x in courses:
    print(x)
if "maths" in courses:
    print("yes,'maths' is in the course list")
courses = ("maths", "english", "geography", "physics", "chemistry")
musa = list(courses)
musa[2]= "economic"
courses= tuple(musa)
    print (x)
courses = {"maths", "english", "geography", "physics", "chemistry"}
for x in courses:
     print (x)
a = 55
b = 55
if b > a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")

a = 55
b = 200
if b > a:
   print("b is greater than a")
elif a==b:
     print("a is equal to b")
else:
    print("a is greater than b")
a = 200
b = 23
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
i = 1
# while i < 0uhy7:
    print(i)
i+=7
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
def company_name():
    print("my company name is piratech")
company_name()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, james):
  print(fname + " " +james)

my_function("Emil", "refuse")

def my_function(fname, lname):
   print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(*kids):
  print("The youngest child is " + "kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**young):
  print("His last name is " + young["first_name"])

my_function(first_name = "Tobias", last_name = "Refsnes")

def my_function(country = "nigerian"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

food = ["apple", "banana", "cherry"]

my_function(food)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

for i in range(1, 12):
    print(i)
def my_function():
    print("this is python")
my_function()
def full_name(name, age):
    print("hello", name )
    print("iam", age)
full_name("john", 33)

def calculator(a, b):
    add = a + b
    return the addition
    return add

call function
take return value in variable
res = calculator(20, 5)
print("Addition :", res)
def even_odd(n):
    # check numne ris even or odd
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd Number')

# calling function by its name
even_odd(20)
# print(randint (10, 20))
def is_even(list1):
    even_num = []
    for n in list1:
        if n % 2 == 0:
            even_num.append(n)
    # return a list
    return even_num

# Pass list to the function
even_num = is_even([2, 3, 42, 51, 62, 70, 5, 9])
print("Even numbers are:", even_num)
def addition(num1, num2):
    # Implementation of addition function in comming release
    # Pass statement 
    pass

addition(10, 2)
 
global_lang = 'DataScience'
def var_scope_test():
      local_lang = 'Python'
      print(local_lang)

var_scope_test()
print(global_lang)
def message(name, class):
    print("hello", name, class)
message(name="faith", class = "SSS")
message(name = "tom",class = "SSS")

def message(name, surname):
    print("Hello", name, surname)

message(name="John", surname="Wilson")
message(surname="Ault", name="Kelly")

name = input("Enter Employee Name: ")
salary = input("Enter salary: ")
company = input("Enter Company name: ")

# Display all values on screen
print("\n")
print("Printing Employee Details")
print("Name", "Salary", "Company")
print(name, salary, company)
number = input("Enter roll number ")
name = input("Enter name ")

print("\n")
print('Roll number:', number, 'Name:', name)
print("Printing type of a input values")
print("type of number", type(number))
print("type of name", type(name))

first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))

print("\n")
print("First Number:", first_number)
print("Second Number:", second_number)
sum1 = first_number + second_number
print("Addition of two number is: ", sum1)
marks = float(input("Enter marks "))
print("\n")
print("Student marks is: ", marks)
print("type is:", type(marks))

import math

# use math module functions
print(math.sqrt(12))

import math, random
print(math.factorial(3))
print(random.randint(20, 30))
import random as rand

print(rand.randrange(10, 20, 2))
from math import *
print(pow(4,2))
print(factorial(5))

print(pi*3)
print(sqrt(100))
import sys

print(sys.path)
import math

print(dir(randint))

frile_object = open('C:/Users/USER/Desktop/bigman/test.txt', 'r')
pint(file_object.read())

file_object = open('C:/Users/USER/Desktop/bigman/pira.txt', 'r')
print(file_object.read())

file_object = open('C:/Users/USER/Desktop/tech.txt', 'a')
print(file_object. Append())
fo = open('C:/Users/USER/Desktop/tech.txt', 'r+')
print(fo.read())

file_object = open('C:/Users/USER/Desktop/tech.txt', 'r')
print(file_object.read())
file_object = open('C:/Users/USER/Desktop/tech.txt', 'a')
file_object. write('\n i love python')
file_object. close()
file_object = open('C:/Users/USER/Desktop/tech.txt', 'r')
print(file_object.read())
file_object. close()
my_file = open(“C:/Users/USER/Desktop/tech.txt”, “r”)
print(my_file.readline(2))
file_object = open('C:/Users/USER/Desktop/tech.txt', 'r')
print(file_object. readlines())
file_object. close()
file_object = open('C:/Users/USER/Desktop/tech.txt', 'a+')
file_object. write('precious is a good boy')
file_object.close()
file_object = open('C:/Users/USER/Desktop/tech.txt', 'a+')
file_object. write('\n precious is a boy')
file_object = open('C:/Users/USER/Desktop/tech.txt','r')
print(file_object. read ())
file_object.close()
file_object =open('C:/Users/USER/Desktop/tech.txt', 'a+')
file_object.write('\n very expensive')
file_object.seek(0)
print (file_object.read())
file_object.close()

my_file =open('love.txt', 'a+')
for i in range(0,3):
     name =input('enter your name:')
     my_file.write(name+ '\n' )
my_file.close()

my_file= open('love.txt', 'w')
love=[]
for i in range(0,3):
    name =input('enter your name:')
    love.append(name+ '\n')
    my_file.writelines(love)
    my_file.close()

with open('love.txt', 'r') as file_object:
    file= file_object.read()
print(file)
file_object.close()

h open('people.csv', 'r') as
 the reader= csv.reader(file)
for row in reader:
    pwitrint(row)


import csv
with open('love.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
import csv
with open('love.csv', 'r',) as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)

import csv
with open('love.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])


my_file=open('me.txt','a+')
for t in range(0,3):
    name=input('enter your surname:')
    my_file. write(name+ '\n')
    my_file.close()



my_file =open('c:/Users/USER/Desktop/tech.txt', 'r')
print(my_file.readlines(-1))


my_file = open('c:/Users/USER/Desktop/tech.txt', 'r')
read_data =my_file.read(1)
print(read_data,end='')
read_data=my_file.read(1)
print(read_data, end='')
read_data=my_file.read(1)
print(read_data,end='')
my_file.close()

my_file = open('C:/Users/USER/Desktop/tech.txt','r')
data = my_file.readlines()
print(data[-1])

my_file = open('C:/Users/USER/Desktop/tech.txt','r')
data = my_file.read()
count = len(data)
print(count)

import os 
os.getcwd()
'C:\Python37'
os.mkdir("MyPythonProject")

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
import json
samuel= {
"name":"timo",
"courses":33,
"university":"kebbi state"
}
samuel=json.dumps(samuel)
print(samuel)

import json
sam = ['orange','mango','banna']
sam=json.dumps(sam)
print(sam)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



import json
with open('abuja.json') as f:
    data = json.load(f)

for district in data['abuja_amac']:
    print(district)
    print(district['name'], district['abbreviation'])


for i in 'chirag':
    print(i)
print('-----')
# list as an iterable
for i in [1, 2, 3]:
    print(str(i*2))


























