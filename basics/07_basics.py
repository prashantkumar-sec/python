#Create a Simple to-do manager
#
# Create an empty list
# Input three Task from user and add into the list
# Then print the whole to-do (Using loop, in numbered format like "1. Task name")

empty_list = []

for i in range(0,3):
    task_name = input("Enter your Task name: ")
    empty_list.append(task_name)


for index, task in enumerate(empty_list , start=1):
    print(f"{index}. {task}")