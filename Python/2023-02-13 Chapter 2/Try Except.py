x = input("enter a number > ")
print(x)
print(type(x))
y = int(x) + 5
print(y)

my_number = input("enter a number > ")
try:
  my_number = int(my_number)
  print(my_number, 'is a number')
except:
  print('Please enter a number')
  print(my_number, 'is NOT a number')
print('done')