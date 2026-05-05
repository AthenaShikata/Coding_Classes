a=5
b=4
c=7
print(a*b)

if a>b or b>c :
  print ('1')
elif a>c :
  print ('2')
else :
  print ('3')

def printsum() :
  print(a + b + c)
printsum()

def generator(n):
  for i in range(n):
    yield 50 + 2*i
it = generator(10)
for i in it : print (i)