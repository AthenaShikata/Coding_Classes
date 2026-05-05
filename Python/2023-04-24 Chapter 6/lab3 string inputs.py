# Python String Lab
# -------------------------------
print('''The goal of this lab is to try getting input.
-----------------------------
Challenge
- How do you do math on an input as a number "str" 
  with an number "int"? 
- Fix the code below so that it 
  does not cause a traceback error
''')      
print('-----------------------------')
myNumber = 100
myInputNumber = input('Enter a number > ')
# add your code below this line
try:
  myInputNumber = int(myInputNumber)
except:
  print(myInputNumber,' is not a number')
  raise TypeError("Only integers are allowed")
myNewNumber = myNumber + myInputNumber
print(myNumber,' + ',myInputNumber,' = ',myNewNumber)
print('----------------------------- \n')