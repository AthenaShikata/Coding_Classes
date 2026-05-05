print('''The goal of this lab is to try out some 
string manipulations & methods.  When you click next, you will see a bunch of .methods that can be used on a string. This lab you will try some out.
-----------------------------')
Don't edit the string 'myString'
Use it as the string you manipulate
-----------------------------''')
myString = '# - Simple 10 word string with the word BANANA'
print('myString = "',myString,'"')
print('----------------------------- \n')
hitAnyKey = input('enter any key to continue > ')
print('''Use the dir(stringVariableName) to see all the methods you can apply to a string
      ''')
print(dir(myString))
print('''
-----------------------------

That looks messy... But does the returned 
structure look familiar?  What is it? It 
has [ ] around it, and has objects separated 
by commas.  What is that? 
      
If you said "A List", then you are right.

Challenge:
- Can you use a FOR loop to print this list 
  of string objects that print out as a column 
  of methods, like:
      
__add__
__class__
__contains__
  ^
  ^
  ^
translate
upper
zfill  
      
Add your code below this line
-----------------------------''')
# add your code below this line

for i in dir(myString):
    print(i)