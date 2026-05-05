print("Evan Peres")
print("2/27/23")


x = input("How old are you?")
try:
  age = int(x)
except:
  print("Please enter a number")
print("You are " + x + " years old")

y = input ("Enter an integer or string")

try:
  z = int(y)
  print(abs(z))
  print(type(z))
except:
  print(len(y))
  print(type(y))

print(max(y))
print(min(y))
a = (1, 3, 5, 10)
print(sum(a))
print(id(y))