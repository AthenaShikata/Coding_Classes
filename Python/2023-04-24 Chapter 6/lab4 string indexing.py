# Python String Lab
# -------------------------------
print('''The goal of this lab is to try out
some string indexing & methods.
-----------------------------
Don't edit the string 'myString'
Use it as the string you manipulate
      
Challenge 
- Print the length of "myString"
- Print the 2nd character of "myString" 
- Print the 4th character of "myString
- What happends if you try to print the 
  27th character of this string?
- Using index slicing, print the text 
  'Banana' character of "myString
''')
myString = 'SimpleOneWordStringBanana'
print('''-----------------------------''')
print('myString = "',myString,'"')
print('''-----------------------------''')
print('# add your code here:')
# add your code here
print(len(myString))
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])
try:
    print(myString[27])
except:
    print('error printing myString[27]')    
print(myString[19:25])
print('end')