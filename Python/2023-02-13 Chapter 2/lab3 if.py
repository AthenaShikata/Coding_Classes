# Python Lab - Introduction to "IF" statements
# Last Edit Jan 30 2023
print('''
This Lab is about the 'IF' statement and how we ask questions.

Hint: Check out W3Schools IF
- https://www.w3schools.com/python/python_conditions.asp
      ''')
x = 12  # Don't change this value
if x > 9 :
  print("x =",x)
  print("The 'if' statement x > 9 was evaluated as 'True'")

# Challenge 1
# Write and play with "IF"
print('''
Challenge # 1
----------------------------------------------------
Run this code, review it, and then change the comparison operation.
      
Ways to compare objects
      
x == y      # x is equal to y
x != y      # x is not equal to y
x > y       # x is greater than y
x < y       # x is less than y
x >= y      # x is greater than or equal to y
x <= y      # x is less than or equal to y
x is y      # x is the same as y
x is not y  # x is not the same as y      

# If you change the comparison operation, remember to change 
it in the print statment too
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
# If you change the comparison operation, remember to change 
it in the print statment too
-------------------------------------------------''')
x = 5
y = 9
z = 12
print("x =",x)
print("y =",y)
print("z =",z)
if x <= y : 
  print("The if statement",x,"<=",y,"was evaluated as 'True'")

if x != z : 
  print("The if statement",x,"!=",z,"was evaluated as 'True'")

if x is z : 
  print("The if statement",x,"is",z,"was evaluated as 'True'")

if x is not y-4 : 
  print("The if statement",x,"is not",y-4,"was evaluated as 'True'")

if x >= y : 
  print("The if statement",x,">=",y,"was evaluated as 'True'")

if x <= z : 
  print("The if statement",x,"<=",z,"was evaluated as 'True'")

if x > z : 
  print("The if statement",x,">",z,"was evaluated as 'True'")