# This program says hello and asks for my name

print('Hello World!') # Hello

print('What is your name?') # Asks for name
name = input()
print('It is nice to meet you ' + name)
print('The length of your name is: ')
print(len(name))

print('What is your age?') # Asks for age
age = input()
print('You will be ' + str(int(age) + 1) + ' in a year')