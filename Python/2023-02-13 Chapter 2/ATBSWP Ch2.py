import math

def spam(num):
  
  try:
    return math.sqrt(num)
  except:
    print("Error")

print(spam(11))
print(spam(92))
print(spam(12))
print(spam(0))
print(spam(-1))
print(spam(4))

print("")
print("")
print("")

import time, sys

indent = 0 
indentIncreasing = True 

try:
    while True: 
        print(' ' * indent, end='')
        print('SUBSCRIBE')
        time.sleep(.1) 

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()