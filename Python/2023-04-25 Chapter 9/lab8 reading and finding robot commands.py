print('''
Using the robot.txt file:
#1 - Create a program, where you ask the 
     user for a variable user_robot_name
#2 - Check to see if the name is in the file
#3 - If it's found, print the line, if not 
     print "Robot Not Found"
#4 - split out all the parts of the line.
HINT: See that the line can be split into a list by commas ','

i.e: 'robot3,rgb-led,green,2022-05-03,08:08:52pm' 

#5 - Using the list you created from step #4, 
     create 5 variables and pull their values by 
     indexing the list
    - robot_name
    - robot_feature
    - robot_action
    - robot_date
    - robot_time
#6 - Print the 5 variables
#7 - Print a formatted line that looks like:
  
The User requested to have <robot_name> turn on 
the <robot_feature> and have it be <robot_action>

# Put your code here:
------------------------------------------
''')
# Put your code here:

#user_robot_name = 'robot1'
user_robot_name = input("Please enter the name of a robot > ")
print(user_robot_name)
print('')

xFile = open('robot.txt')
for line in xFile:
    line = line.rstrip()
    if line.startswith(user_robot_name) is False:
        print('Robot Not Found')
    elif line.startswith(user_robot_name) is True:
        print(line)
        line_items = (line.split(','))
        print(line_items)
        robot_name = line_items[0]
        robot_feature = line_items[1]
        robot_action = line_items[2]
        robot_date = line_items[3]
        robot_time = line_items[4]
        print(robot_name,robot_feature,robot_action,robot_date,robot_time)
        print('The User requested to have',robot_name,'turn on the',robot_feature,'and have it be',robot_action)