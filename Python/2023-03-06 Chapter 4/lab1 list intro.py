# Python LIST Lab1
print('''
Python Lists - Introduction 
Lists are comma delimited groups of variables

Challenge #1
Run the code, make sure you understand how the list is constructed
      
- Can you explain the difference between a single object 
  variable and a list?
  Single objects have one value inside of them. Lists have a groups of multiple, addressable values.
- Can you explain how lists are comma delimited sets of objects?
  Lists are a group of objects inside []. The different objects are seperated by commas. 
      ''')

# x = a single object
print('''x = 9
x is a single variable object''')
x=9
print(x)
print(type(x))
# x = a list of objects
x = [1, 2, 5, 66, 42, 19]
print('\nx = ',x,'x is now a list of objects')
print(x)
print(type(x))
# x = a list of mixted Type objects
x = ['fName', 'lName', 25, True, 4.2]
print('\nx = ',x,'x is now a list of mixed objects')
print(x)
print(type(x))
# Challenge 2
print('''
Challenge #2 
- Create a new list of integers
- Create a new list of character strings
- Create a new list of mixed integers, floats, and strings

Enter your code here:
------------------------------------
''')
listINT = [1, 2, 97, 42]
listSTR = ['lol', 'lmao', 'lmfao', 'oof', '69420']
listMIX = ['haha', 1, 19, '27', [3.14159, 99999999999]]
print(listINT)
print(type(listINT))
print(listSTR)
print(type(listSTR))
print(listMIX)
print(type(listMIX))
print('------------------------------------')