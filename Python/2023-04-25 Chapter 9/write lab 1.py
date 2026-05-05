import os
# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and 
reading the whole file into a big string.

You can read a file line by line, or put the 
whole file in as a single string.  

After you read the file in, write it out to some 
new files using the "w" and "a" modes
      ''')
# Challenge 1
# Open the file matrix.txt and write out a new file matrix2.txt"
print('''
Challenge # 1
----------------------------------------------------
Open the file matrix.txt and write out a new file 
"matrix2.txt" 
- https://www.w3schools.com/python/python_file_open.asp
---
''')
# -----------------------------

def challenge1():
    try:
        open('matrix.txt','r')
    except: 
        raise TypeError('File Does Not Exist')
    xFile1 = open('matrix.txt','r')
    cache = xFile1.read()
    xFile2 = open('matrix2.txt','w')
    xFile2.write(cache)
    xFile1.close()
    xFile2.close()


# -----------------------------

# Challenge 2
# Open the file matrix.txt and write out a new file called matrix3.txt that has a new first line that says "New First Line"
print('''
Challenge # 2
----------------------------------------------------
Open the file matrix.txt and write out a new file 
called "matrix3.txt" that has a new first line that 
says "New First Line" 
- https://www.w3schools.com/python/python_file_open.asp
---
''')
# -----------------------------

def challenge2():
    try:
        open('matrix.txt','r')
    except: 
        raise TypeError('File Does Not Exist')
    xFile1 = open('matrix.txt','r')
    cache = xFile1.read()
    xFile2 = open('matrix3.txt','w')
    xFile2.write('New First Line\n'+cache)
    xFile1.close()
    xFile2.close()

# -----------------------------

# Challenge 3
# Open the file matrix.txt and write out a new file called matrix4.txt that has a new first line that says "New First Line" and then has a new last line that says "New Last Line"
print('''
Challenge # 3
----------------------------------------------------
Open the file matrix.txt and write out a new file 
called "matrix4.txt" that has a new first line that 
says "New First Line" and then has a new last line 
that says "New Last Line" 
- https://www.w3schools.com/python/python_file_open.asp
---
''')
# -----------------------------

def challenge3():
    try:
        open('matrix.txt','r')
    except: 
        raise TypeError('File Does Not Exist')
    xFile1 = open('matrix.txt','r')
    cache = xFile1.read()
    xFile2 = open('matrix4.txt','w')
    xFile2.write('New First Line\n'+cache+'\nNew Last Line')
    xFile1.close()
    xFile2.close()

# -----------------------------


def main():
    challenge1()
    challenge2()
    challenge3()

main()