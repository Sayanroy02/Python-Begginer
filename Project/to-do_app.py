"""
To do app 
we will do 
C - create task
R - Read task
U- Update Task
D- Delete Task

will ask you contiounsly till user will exit the program
"""

def task():
    tasks =[] # empty list
    print("------- WELCOMETO THE TASK MANAGEMENT APPLICATION ----------")
    total_task = int(input("Enter how many task you want to add ?\n "))
    for i in range(1, total_task+1):
        task_name= input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Todays task are \n{tasks}")

    while True:
        operation = int(input("Enter number\n1-Add\n2- Update\n3-delete\n4-View\n5-Stop\n"))
        if operation == 1:
            add = input("Enter task = ")
            tasks.append(add)
            print(f"your task - {add} , added successfully.")
        elif operation == 2 :
            updated_val = input("Enter the task name you want to update\n")
            # we will use membership operator (in , not in)
            if updated_val in tasks:
                update= input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = update
                print(f"Updated task is {update}")
            else:
                print(f"{updated_val} is not in task !")
        elif operation == 3:
            delete_value = input("What do you want to delete ?\n")
            if delete_value in tasks:
                ind = tasks.index(delete_value)  #taking index number of the value entered by user 
                del tasks[ind]  #deleting task from index number 
                print(f"task - {delete_value} has been deleted ")
            else:
                print(f"{delete_value} is not in task !")
        elif operation ==4 :
            print(f"total tasks = {tasks}")

        elif operation == 5:
            print("closing the program....\nHave a nice day ahead !")
            break  # stopping the program
    else:
            print("Invaild input")

task()
