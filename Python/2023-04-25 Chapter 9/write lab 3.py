print('''
Using the robot.txt file:

1) Open the file robot.txt as read only

2) Open another file robot2.0.txt as append, 
so you can write to it.

3) Read robot .txt in one line at a time

4) Split the line into a list using the "," as a split parameter

5) Check to see if the second item on your list is "rgb-led". 
   -- If it is not, then write the line back out unchanged 
      to your new file
      
6) If it's found, check the next item   on the list, and see 
if it is a color like "red", green" blue" (how could you 
check a list of colors? maybe create a list of colors you 
can compare to)
  -- If it's one of the colors on your list, then write the 
     line back out unchanged to your new file
  -- Write out with the color changed to #FFFFFF if the color 
     is NOT on your color list
     
7) If it's found, check the next item on the list, and see if it has a # and does not have any ":" in the string.
  -- if it has #, but not ":", then write the line back out 
     unchanged to your new file

8) If it's found, check the next item on the list, and see if it has a # and does not have any ":" in the string.
  -- if it has #, and ":", then edit the format to remove the ":" 
     and then write the line back out to your new file

Example:

robot2,rgb-led,green,2021-05-24,09:53:49pm <-- Write out unchanged if the color is on your color list

robot2,rgb-led,forest,2021-05-24,09:53:49pm <-- Write out with the color changed to #FFFFFF if the color is NOT on your color list
robot2,led-3,on,2021-05-24,09:55:11pm <-- Write out unchanged
robot1,rgb-led,#FFFFFF,2022-05-03,01:59:55pm <-- Write out unchanged

robot2,rgb-led,#FF:00:FF,2022-05-03,03:57:30pm <-- Write out as #FF00FF, where you striped the ":" out of the list item





# Put your code here:
------------------------------------------
''')

colors_Allow = ('green', 'red', 'blue',)
colors_Disallow = {'orange':'#FFA500',  
          'forest':'#228B22', 
          'yellow':'#FFFF00', 
          'pink':'#FFC0CB', 
          'blart':'#AD58D6'}

xfile1 = open('robot.txt')
xfile2 = open('robot2.txt','w')
for line in xfile1:
    #print(line)
    line_items = line.strip('\n[]<>();')
    #print(line_items)
    line_items = line_items.split(',')
    #print(line_items)
    if line_items[1] == 'rgb-led' :
        if line_items[2] in colors_Allow:
            xfile2.write(line)
        elif line_items[2] in colors_Disallow:
            line_items[2]=colors_Disallow[line_items[2]]
            line=','.join(line_items)
            xfile2.write(line)
        else:
            if line_items[2].startswith('#') == True:
                if line_items[2].find(':') == -1:
                    xfile2.write(line)
                else:
                    hexSplit = line_items[2].split(':')
                    line_items[2]=''.join(hexSplit)
                    line=','.join(line_items)
                    xfile2.write(line)
    else:
        xfile2.write(line)


xfile1.close()
xfile2.close()