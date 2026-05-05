print('''The goal of this lab is to try out some 
string manipulations & methods.  
-----------------------------')
Don't edit the string 'myString'
Use it as the string you manipulate
-----------------------------''')
myEmailString = 'This is a string with emails in it, like jim.The.STEAM.Clown@gmail.com or jburnham@metroed.net or even topClown@STEAMClown.org split them out and print only the emails'

print('''-----------------------------

Challenge: 
- Use the .split command and the .find() method to print just the emails in the "myEmailSting"

Hint: When you use the .split method, you take the string and write it to a new variable that is a list of the .split() Objects.
''')

print('''
Add your code below this line
-----------------------------''')
print('myEmailString = "'+myEmailString+'"')
print('''
You want output like:
  jim.The.STEAM.Clown@gmail.com
  jburnham@metroed.net
  topClown@STEAMClown.org
      ''')
# add your code below this line

myEmails = []
myList = myEmailString.split()
print(myList)
print('')
for i in myList:
   x = i.find('@')
   if x > 1: #1 sorts out random @ characters so that the @ must be within the word itself
      myEmails.append(i)
print(myEmails)