print('''The goal of this lab is to try out some 
string manipulations & methods.  
-----------------------------')
Don't edit the string 'myString'
Use it as the string you manipulate
-----------------------------''')
mySpaceString = '    This string     has lots of        spaces      in it.     Remove them.        '

print('''-----------------------------

Challenge: 
- Use a the .rstrip() and .lstrip() to 
  strip the white space from the beginning 
  and the end and print out the new string.  
- What if you just used .strip? 
- How is .strip() diffrent than .rstrip() and .lstrip()
.strip() does the job of both .rstrip() and .lstrip()
''')

print('''
Add your code below this line
-----------------------------''')
print('mySpaceString = "',mySpaceString,'"')
# add your code below this line

print('')
print(mySpaceString.rstrip().lstrip())
print('')
print(mySpaceString.strip())
print('')
li=mySpaceString.split()
print(' '.join(li))