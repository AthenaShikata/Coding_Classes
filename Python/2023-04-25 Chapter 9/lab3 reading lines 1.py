# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, line by line using the file method: 
- file_handle = open(file_name) method
      ''')
# Challenges
print('''
Challenge #1 & #2
----------------------------------------------------
#1 - Edit the code below to count each line, 
     and print the total out at the end
      
#2 - Edit the code below to open the mbox-short.txt file
---
''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')
# -----------------------------
fhand = open('matrix.txt')
# Need a variable to count the lines
count=0
for line in fhand:
    # Need to increment the line count Variable
	print(line)
	count = count + 1
print('Line Count:', count)
print('''
-------------------------------------------------''')
