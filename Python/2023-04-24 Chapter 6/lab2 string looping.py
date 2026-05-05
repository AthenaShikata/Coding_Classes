# Python String Lab #3
# -------------------------------
print('''The goal of this lab is to try using 
loops to index a string.
-----------------------------
Challenge
- Use a WHILE loop to print out "myString" 
  one character at a time.
- Then, also implement it using a FOR loop
- Is a While loop or a For loop better?  Why?
A for loop is better because the code is much simpler.
      
Add your code below this line
-----------------------------''')
myString = 'SimpleOneWordStringBanana'
print(myString)
# add your code below this line

print('')

i=0
while i < len(myString):
    print(myString[i])
    i+=1

print('')

for j in (myString):
    print(j)