task = []
while True :
    print("--------------------------------------------------------------------------------")
    print("Welcome to the task manager")
    print("Enter your choice")
    print("1-Number (1) to add a task")
    print("2-Number (2) to show all tasks")
    print("3-Number (3) to delete a task")
    print("4-Number (4) to exit")
    print("--------------------------------------------------------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task.append(input("Enter the task name: "))
    elif choice == 2:
        print("Task List")
        for i in range(len(task)):
            print(i+1,"-",task[i])
    elif choice == 3:
        print("Enter the task number to delete: ")
        input = int(input("Enter your choice: "))
        del task[input-1]
    elif choice == 4:
        print("Thank you for using the task manager")
        break
    else:
        print("Invalid choice")
