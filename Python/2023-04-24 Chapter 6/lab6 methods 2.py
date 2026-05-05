print('''The goal of this lab is to try out some 
string manipulations & methods.  
-----------------------------')
Don't edit the string 'myString'
Use it as the string you manipulate
-----------------------------''')
myString = '# - Simple 10 word string with the word BANANA'
print('myString = "',myString,'"')
print('''-----------------------------
See all the methods you can apply to a string
      ''')
for i in dir(myString):
  print(i)
print('''
-----------------------------

Challeng #1 
- Scroll back up to see some of the methods.  
- Please apply the following methods to the "myString"
  - .upper 
  - .lower
  - .find <-- Find the '10'
  - .startswith <-- Find the '#'
  - Pick 3 more to try
''')
print('Here is the .title() method')
myMethodString = myString.title()
print('myMethodString =', myString)
print('myMethodString =', myString.title())
print('''
Add your code below this line
-----------------------------''')
# add your code below this line

print(".upper")
print(myString)
print(myString.upper())
print('')
print(".lower")
print(myString)
print(myString.lower())
print('')
print(".find")
print(myString)
print(myString.find('10'))
print('')
print(".startswith")
print(myString)
print(myString.startswith('#'))
print('')
print("swapcase")
print(myString)
print(myString.swapcase())
print('')
print(".split")
print(myString)
print(myString.split())
print('')
print(".islower")
print(myString)
print(myString.islower())
print('')
print(".isupper")
print(myString)
print(myString.isupper())
print('')