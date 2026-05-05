# Python Dictionaries
print('''
Python Dictionaries - Lists vs. Dictionaries 
Dictionaries are Key:Value pairs of objects in 
a list like structure.

Challenge #1
Run the code, Explain the difference between lists and dictionaries
A list is a set of values that is indexed by their order in the list. A dictionary is a set of key:value pairs that is indexed by the key.

- See that the list is index'able
- See that the Dictionary is a keyword:value pair

- How do you "index" a dictionary?
By calling for the keys which returns their value pair

- Add an additional key:value pair to the ddd dictionary
  Imagine that this is a dictionary for a college engineering class.  
  Does it have a lab? 'lab':'true' , add a short description for 
  the class. 'description':'short string describing the class'

      ''')

lst = list()
lst.append(183)
lst.append("2:00 PM")
print(lst)
lst[1] = "3:00 PM"
print(lst)
print(lst[1])

ddd = dict()
ddd['course'] = 182
ddd['time'] = "2:00 PM"
print(ddd)
ddd['time'] = "3:00 PM"
ddd['lab'] = 'True'
ddd['description'] = 'short string describing the class'
print(ddd)
print(ddd['time'])