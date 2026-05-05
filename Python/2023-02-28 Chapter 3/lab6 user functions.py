# Functions - Passing Arguments
print('''Functions - Passing Arguments
Learn more about Functions here:
https://www.w3schools.com/python/python_functions.asp
''')      
print('''
Challenge #1
Can you follow and explain
- How arguments are passed from the main code to the function?
The functions specify arguments to use and those arguemnts are passed from main when the function is executed in main with those arguments.
- Can you explain how a value is 'returned'
The return function specifies what value to output after the function completes.
      ''')
print('''
----------------------------------------------------
''')

def my_math(x,y) :
  z=x+y
  return z

def main():
  my_num_1 = 3
  my_num_2 = 6
  my_operation = '+' # +, -, *, or /
  sum = my_math(my_num_1, my_num_2)
  product = chal2(my_num_1,my_num_2)
  c3 = chal3(my_num_1,my_num_2)
  c4 = chal4(my_num_1,my_num_2,my_operation)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)
  print("The product of", my_num_1, "x", my_num_2, "=",product)
  print("The result of Challenge 3, given ", my_num_1, "&", my_num_2, "is",c3)
  print("The result of ", my_num_1, my_operation, my_num_2, "is",c4)

print('''
Challenge #2
Create a function that multiplies 2 numbers and returns the result''')
# Enter Code Here:
def chal2(x,y) :
  z=x*y
  return z

print('''
Challenge #3
Create a function that adds 2 numbers and if the result is odd, adds 1, then returns the result
Enter Code Here:''')
# Enter Code Here:
def chal3(x,y) :
  z=x+y
  if (z % 2) == 0: 
    return z 
  else: 
    return (z + 1)
  
print('''
Challenge #4
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result
Enter Code Here:''')
# Enter Code Here:
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

print('''
----------------------------------------------------
''')

main()