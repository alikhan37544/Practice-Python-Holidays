tasks = []

def display_menu():
    print("To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number > 0 and task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
