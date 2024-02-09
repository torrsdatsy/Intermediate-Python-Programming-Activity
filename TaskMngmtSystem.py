tasks = []

#function to add a new Task.
def add_task():
    name = input("Enter task name:  ")
    description = input("Enter Description:  ")
    duration = int(input("Enter Duration(in minutes): "))
    task = {'name': name, 
            'description': description, 
            'duration': duration, 
            'status' : 'Pending'
        
    }
    tasks.append(task)

#function to display a new task.
def display_task():
    print("\nDisplay task")
    for index, task in enumerate(tasks, start =1):
        print(f"Task {index}: ")
        print(f"Task Name: {task['name']}")
        print(f"Task Description: {task['description']}")
        print(f"Task Duration: {task['duration']}")
        print(f"Task Status: {task['status']}")
        print()


# Function to update the status of a specific task
def update_task():
    task_name = input("Enter the name of the task to update status: ")
    
    # Check if the task exists
    found = False
    for task in tasks:
        if task ['name'] == task_name:
            found = True
            new_status = input("Enter the new status (In-Progress or Completed): ")
            #Validate the new status.
            if new_status == 'In-Progress' or new_status == 'Completed':
                task['status'] = new_status
                print(f"Status of task {task_name} updated to {new_status}!")
            else:
                print("Invalid Status. Should be 'In-Progress' or 'Completed'!")
            break
    
    #if the task name is not found.    
    if not found:
        print(f"Task {task_name} not found!")
        
#function to calculate status and to display the names of the status.
def display_tasks_by_status(status):
    total_duration = 0
    tasks_with_status = []
    for task in tasks:
        if task['status'] == status:
            tasks_with_status.append(task)
            total_duration += task['duration']

    print(f"\nTasks with status '{status}':")
    if tasks_with_status:
        for index, task in enumerate(tasks_with_status, start=1):
            print(f"{index}. Task Name: {task['name']}, Duration: {task['duration']} minutes")
        print(f"Total Duration for '{status}' tasks: {total_duration} minutes")
    else:
        print(f"No tasks found with status '{status}'")



#function to define main menu.
def main():
    print("Welcome to the Task management System!")
    print("1. Add New Task")
    print("2. Display All Tasks")
    print("3. Update Tasks")
    print("4. Display all Pending tasks")
    print("5. Display all In-progress tasks")
    print("6. Display all Completed tasks")
    print("7. Exit!")
    
    #Selection of the number that input.
    while True:
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            add_task()
        elif choice == 2:
            display_task()
        elif choice == 3:
            update_task()
        elif choice == 4:
            display_tasks_by_status('Pending') 
        elif choice == 5:
            display_tasks_by_status('In-Progress')
        elif choice == 6:
            display_tasks_by_status('Completed')
        elif choice == 7:
            print("Thank You!")
            break
        else:
            print("Invalid Input")
    
main() #passing to the function

