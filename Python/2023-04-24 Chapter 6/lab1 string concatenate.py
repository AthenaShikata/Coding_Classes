# Python String Lab #2
# -------------------------------
print('''The goal of this lab is to try out
some string indexing & methods.
Link: https://www.w3schools.com/python/python_strings_slicing.asp
-----------------------------
Don't edit the string 'myString'
Use it as the string you manipulate
# https://www.youtube.com/watch?v=5MJLi5_dyn0
      
Challenge #1
- Use the concatenate operator to combiine following strings''')
myString = 'Bo-ber-ley bo-na-na fanna'
myStringOne = 'Bo-ber-ley'
myStringTwo = 'bo-na-na'
myStringThree = 'fanna'      
print('\t',myStringOne,'\n\t', myStringTwo, '\n\t', myStringThree)
print('''  into a new variable, and print that single string with
  3 "words" in it.''')
print('\nYou want it to look like this:\n',myString)
print('''
hint: you might need to add some spaces when you concatenate

- How long is the new string? Use len()''')
print('''-----------------------------''')
print('# add your code here:')
# add your code here

myString = myStringOne + " " + myStringTwo + " " + myStringThree
print(myString)