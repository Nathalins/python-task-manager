


"""
Task Manager

Summary:
My program is a Task Manager that helps manage responsibilities
in work, education, and daily activities. This program will read from the 
tasks.txt file, which contains a list of additional tasks, their completion 
status, and their priority levels. This program will separate the tasks into 
completed and incomplete categories by being displayed in an organized manner.

Incompleted tasks are organized
by priority level(high, medium, or low), which makes it easier for the 
user to see which is important
responsibilities to complete.

The user can add as many tasks as needed and also update the previous tasks.
If the user adds a task that already exists in the file,
it will be replaced with a complete one. 
This way makes it more organized. Completed tasks don't need a priority, since
It's already work done.

Lastly, the program calculates the average completion rate of all the completions
task and outputs a summary to grab the attention of their programs and to track them.
"""


#1. Storing the tasks.txt in a list
#--------------------------------

tasks_list = [] #empty list to store the tasks from file
file = open("tasks.txt", "r") #to open the file

# For output inside of the file
for task_entry in file:
    task_entry = task_entry.strip() #removing new lines or spaces
    items = task_entry.split(",") #split into task, status, priority
    
    if len(items) < 3:
        continue # if there is error skip 
    
    # Each items to store which is first, second and third
    task = items[0].strip().lower()
    status = items[1].strip().lower()
    priority = items[2].strip().lower()
    
    # adding the task list as [task, status, priority]
    tasks_list.append([task, status, priority])
    
file.close() 

#2. Counting for the completed task to get the average of it
#----------------------------------------------------------

#To store the count
complete_total = 0
incomplete_total = 0

for item in tasks_list:
    if item[1] == "complete":
        complete_total += 1
    else:
        incomplete_total += 1


#Function : Average complete
def average_complete(done, total):
    average = (done / total) * 100
    return average


#3. User adds the task or updates of it
#-------------------------------------

#While Loop for the user input in addition until they're done
while True:
    task = input("Add your task and if you're done then enter 'done' ': ")
    
    if task.lower() == "done":
        break
    
    status = input("Enter complete or incomplete: ")
   
    
   
    #Checking if it's incompleted to add the priority
    if status.lower() == "incomplete":
        priority = input("Enter the priority (high, medium or low): ")
    else:
        # completed tasks don't need priority
        priority = "none" #no value and no print
        
        

    # remove the same previous tasks from the tasks file
    removed_status = None
    for t in tasks_list:
        if t[0].lower() == task.lower(): 
            removed_status = t[1]
            tasks_list.remove(t)
            break
    
    # fix the counters after removing a task
    if removed_status == "complete":
        complete_total -= 1
    elif removed_status == "incomplete":
        incomplete_total -= 1
    
    # Uptading the tasks
    tasks_list.append([task.lower(), status.lower(), priority.lower()])


    # update counts
    if status.lower() == "complete":
        complete_total += 1
    else:
        incomplete_total += 1

#4. Organizing the tasks into grouping
#---------------------------------------

#To store
completed_list = []
incompleted_list = []


for item in tasks_list:
    if item[1] == "complete":
        completed_list.append(item)
    else:
        incompleted_list.append(item)


#Priority of incompleted group        
incompleted_high = []
incompleted_medium = []
incompleted_low = []


for item in incompleted_list:
    if item[2] == "high":
        incompleted_high.append(item)
    elif item[2] == "medium":
        incompleted_medium.append(item)
    else:
        incompleted_low.append(item)      
        
#Step 5: Printing the Output
#------------------------------

#To organize
print("")
print("COMPLETED TASKS:")
print("----------------")

for item in completed_list:
    print("-", item[0])
print("")


print("")
print("")


print("INCOMPLETE TASKS:")
print("----------------")

print("Highest priority:")
for item in incompleted_high:
    print("-", item[0])
print("")


print("Medium priority:")
for item in incompleted_medium:
    print("-", item[0])
print("")


print("Lowest priority:")
for item in incompleted_low:
    print("-", item[0])
print("")

    
print("")

# Average Completed
total = complete_total + incomplete_total
average_complete = average_complete(complete_total, total)
print("----------------------------------------------")
print("Your Average Complete Work:", average_complete)
print("----------------------------------------------")



