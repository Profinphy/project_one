import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

import re
string = 'twelve:12 Eighty:45 nine:89.'
pattern = re. compile('\d+')
matches = pattern.split(string)
for match in matches:
  print(match)


import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

import re
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

number_iterator = iter([1, 2, 3, 4, 5])
print(type(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
# Once the iterator is exhausted, next() function raise StopIteration.
print(next(number_iterator))



precious =[]
for i in range(1,101):
    precious.append(i**2)
print(precious)

precious =[i**2 for i in range(1,101)]
print(precious)

example with an if clause
create a list of movies starting with the letter G.

movies =['star wars', 'Gandhi', 'casablance', 'shawshant Redemption', 'Toy story', 'Gone with the kind','citizen kane','it\'s wooderful life', 'the wizard of oz', 
'Gattace', 'Rear windom', 'Ghostbusters', 'To KILL A Mockingbird', 'Good Will Hunting', '2001: A space odyssey', 'Rarders of the lost Art', 'Groundhog Day', 'close Encounters of the third kind']

gmovies =[]
for tithe in movies:
    if tithe.startswith('G'):
        gmovies.append(tithe)
print(gmovies)

gmovies =[tithe for tithe in movies if tithe.startswith('G')]
print(gmovies)

import datetime
yello =datetime.datetime(2023,4,17)
print(yello.strftime('%w'))














