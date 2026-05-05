# Finding Stuff
print('''
Use the String Methods to find stuff

  1) Can you find all the lines that start with "From:"
  2) What about line that start with "To:"
  3) Find all the lines with an email addresses
    - How would you find them?
    - Hint: split the line into a list of "words" then look for emails
  4) Dates? Can you find the line with the oldest "Date" 'Date: 2008-01-04 11:11:00 -0500 (Fri, 04 Jan 2008)'
    - Same Hint an 3
      
      ''')
xfile = open('mbox-short.txt')
for line in xfile:
    line=line.rstrip()
    if line.startswith('From: '):
        print(line)
    if line.startswith('To: '):
        print(line)
print('')
xfile = open('mbox-short.txt')
for line in xfile:
    line=line.rstrip()
    if line.find('@') != -1:
        print(line)