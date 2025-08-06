tasks = []

def show_tasks():
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def delete_task():
    show_tasks()
    task_number = int(input("Enter the number of the task to delete: "))
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid task number.")

def todo_list():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()
