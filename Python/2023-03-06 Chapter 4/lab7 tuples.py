print('''
Update the function to pass a tuple of random 
length set of numbers, and then return the 
same 2 values in a tuple
      
Hint: Pass a tuple set as a single argument, 
find the len() and then loop through the 
tuple for the values
''')

def sum_and_avg1(*values):
    s=0
    for i in values:
        s += i
    a=s/3
    return (s,a)

sa=sum_and_avg1(19, 25, 42,)
print(sa)
print(type(sa))
(sum, avg) = sa
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))

print('''

method 2

''')

def sum_and_avg(t):
    s=0
    l=len(t)
    for i in range(l):
        s += t[i]
    a=s/l
    return (s,a)

tu = (19, 25, 42,)
sa2=sum_and_avg(tu)
print(sa2)
print(type(sa2))
(sum, avg) = sa2
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))