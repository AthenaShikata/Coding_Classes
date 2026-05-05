# Functions - Passing Arguments
print('''Functions - Passing Arguments
Learn more about Functions here:
https://www.w3schools.com/python/python_functions.asp
''')      
print('''
Challenge #4
Run this code, then edit
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result

Print the math operation and then the resulting equation

Enter Code Here:
----------------------------------------------------      ''')
# Edit and Enter Code Here:
def chal4(x,y,z) :
  if z == '+' :
    a = x+y
  elif z == '-' :
    a = x-y
  elif z == '*' :
    a = x*y
  elif z == '/' :
    a = x/y 
  return a

def my_math(x,y) :
  z=x+y
  return z

def main():
  test = True
  test_num1 = True
  test_num2 = True
  test_operation = True
  while test :
    while test_num1 :
      my_num_1 = input('Enter an integer: ')
      print('1',my_num_1)
      try :
        my_num_1 = int(my_num_1)
        test_num1 = False
      except: 
        pass
    while test_num2 :
      my_num_2 = input('Enter an integer: ')
      print('2',my_num_2)
      try :
        my_num_2 = int(my_num_2)
        test_num2 = False
      except :
        pass
    while test_operation :
      my_operation = input('Enter +, -, *, or / ')
      print('op',my_operation)
      try :
        if my_operation == '+' : test_operation = False
        elif my_operation == '-' : test_operation = False
        elif my_operation == '*' : test_operation = False
        elif my_operation == '/' : test_operation = False
        else : raise TypeError("Only + - * / are allowed")
      except :
        pass
    test = False
  '+' # +, -, *, or /
  sum = my_math(my_num_1, my_num_2)
  c4 = chal4(my_num_1,my_num_2,my_operation)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)
  print("The result of ", my_num_1, my_operation, my_num_2, "is",c4)

print('''
----------------------------------------------------
''')
print('''
Challenge #5
in the main() function, add an input() request to get the x,y values.
- make sure they are numbers.
- in a while loop keep asking for the 2 values if one or both are 
  not a number
- make sure you do valid Error and Exception testing.
    ''')

main()