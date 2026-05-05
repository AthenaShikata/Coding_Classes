print('''The goal of this lab is to try out some 
string manipulations & methods.  
-----------------------------')
Don't edit the string 'myString'
Use it as the string you manipulate
-----------------------------''')
mySpaceString = '    This string     has lots of        spaces      in it.     Remove them.        '

print('''-----------------------------

Challenge: Use methods, Loops, and functions 
to strip the extra spaces in the sentence and 
make it look like a normal sentence and print 
out the new string
''')

print('''
Add your code below this line
-----------------------------''')
print('mySpaceString = "',mySpaceString,'"')
# add your code below this line

print('Methods')
li=mySpaceString.split()
print(' '.join(li))
print('')

print('Loops')
('''myLoopString = [0]
count = 0
for i in mySpaceString.strip():
    if i == ' ':
        if x == 0:
            myLoopString[count] = i
            x=1
    else:
        myLoopString[count] = i
        x=0
    count = count + 1
    ''')
newString = ''
lastChar = ''

for char in mySpaceString:
    if char != ' ' or lastChar != ' ':
        newString += char
    lastChar = char
    
if newString[0] == ' ':
    newString = newString[1:]
if newString[-1] == ' ':
    newString = newString[:-1]

print(newString)

print('')

print('Functions')
def normalize(i):
    temp=i.split()
    print(' '.join(temp))
normalize(mySpaceString)
print('')