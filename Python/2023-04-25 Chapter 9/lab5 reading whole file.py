# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and 
reading the whole file into a big string.

You can read a file line by line, or put the 
whole file in as a single string.  This is an example 
of reading the whole file using the file method: 
- file_handle.read() method
      ''')
# Challenge 1
# Find the index that will print "red pill"
print('''
Challenge # 1
----------------------------------------------------
Play with indexing the string to find the index 
location for "red pill" and print the location index 
and text "red pill" here:
      
Hint: You could find it by trial and error, or you 
could use a string method like .find() 
- https://www.w3schools.com/python/ref_string_find.asp
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
-------------------------------------------------''')
# -----------------------------
xfile = open('matrix.txt')
whale = xfile.read()
print('Location of "red pill" =', whale.find('red pill'))
print('Number of Characters =',len(whale))
print(whale[80:89])
# Find the index location for the text "red pill" and print the location index and text "red pill" here:
print('''
-------------------------------------------------''')
