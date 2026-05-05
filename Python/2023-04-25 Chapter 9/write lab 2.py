# Opening File Handles and reading data from files
print('''
This Lab is about opening a file to read,
and then be able to write it out, with changes.
(Maybe make a back up first.) 
      ''')
# Challenge 1
# Open the file matrix.txt, Read it, and then write it out again with some diffrences to matrix.txt"
print('''
Challenge # 1
----------------------------------------------------
Open the file matrix.txt in "r" mode, read it, and 
then open it again in "w" mode and write out a new 
file "matrix.txt" (Tip: Maybe write a backup before 
you write over the original matrix.txt)

1) Find the text "blue pill" and change it to 
something ridiculous.

2) Find the text "red pill" and change it to something 
equally ridiculous.

3) Write the edits back out the the same matrix.txt file.

- https://www.w3schools.com/python/python_file_open.asp
---
''')
# -----------------------------

try:
    open('matrix.txt','r')
except: 
    raise TypeError('File Does Not Exist')
xFile1 = open('matrix.txt','r')
cache = xFile1.read()
print(cache)
xFile2 = open('matrix.txt','w')
cache = cache.replace('blue pill','sussy baka')
print(cache)
cache = cache.replace('red pill','chad wojack')
print(cache)
xFile2.write(cache)
xFile1.close()
xFile2.close()