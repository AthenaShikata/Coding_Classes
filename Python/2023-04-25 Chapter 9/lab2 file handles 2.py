# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and 
printing the file handle.

Hint: Check out W3Schools File Handling
- https://www.w3schools.com/python/python_file_handling.asp
      ''')
# -----------------------------
print('''
Challenge
----------------------------------------------------

What happends if the file does not exist? 
- Try opening a file that does not exist... 
Like "matrix2.txt"
you get a traceback error if you try this

Can you open a diffrent file? 
- Try opening the file "mbox-short.txt"
---
''')
# -------------------------------------------------
print('''Answer to Challenge
-------------------------------------------------''')
# Try opening a file that does not exist... Like "matrix2.txt"
xfile = open('matrix.txt')
print(xfile)
print('''
-------------------------------------------------''')
xfile2='matrix2.txt is error'
print(xfile2)
xfile3 = open('mbox-short.txt')
print(xfile3)