# Open the text files mbox-short.txt, read in each line, find all the emails, and print out a list of emails.
print('''Open the text files mbox-short.txt, read in each line,
find all the emails, add them to a new list,
and print out a list of emails.

#1 - look at each line
#2 - If the line has an Email in it
    - How would you find them?
    - Hint: split the line into a list of "words" then look for emails

  'From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl'    

#3 - strip the email
  'stephen.marquard@uct.ac.za'      
      
Open the mbox-short.txt first, then try the 
mbox-medium.txt befor you try mbox.txt

# Add Your Code Here:
------------------------------------------------
      ''')
# Add Your Code Here:
count = 0
email_list=[]
xfile = open('mbox.txt')
print(xfile)
print('')
for line in xfile:
    line = line.rstrip()
    line_items = line.split()
    for i in line_items:
        if i.find('@') != -1:
            print(i.strip('<>();'))