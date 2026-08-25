tasks = []

while True:
    print("-" * 50)
    print("Welcome to the Task Manager")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Exit")
    print("-" * 50)
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        new_task = input("Enter the task name: ")
        tasks.append(new_task)
        print(f"'{new_task}' added successfully!")
        
    elif choice == 2:
        if not tasks:
            print("Your task list is empty.")
        else:
            print("\n--- Your Tasks ---")
            for i in range(len(tasks)):
                print(f"{i + 1} - {tasks[i]}")
                
    elif choice == 3:
        if not tasks:
            print("No tasks available to delete.")
        else:
            delete_index = int(input("Enter task number to delete: "))
            if 1 <= delete_index <= len(tasks):
                removed = tasks.pop(delete_index - 1)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid task number.")
                
    elif choice == 4:
        print("Thank you for using the task manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
