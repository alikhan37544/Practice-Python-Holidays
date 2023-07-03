class TaskManager:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index + 1}. [{status}] {task['description']}")

    def add_task(self):
        task_description = input("Enter the task description: ")
        task = {"description": task_description, "completed": False}
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to edit: "))
        if task_number > 0 and task_number <= len(self.tasks):
            new_description = input("Enter the new task description: ")
            self.tasks[task_number - 1]["description"] = new_description
            print("Task edited successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if task_number > 0 and task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        if task_number > 0 and task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.edit_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_completed()
            elif choice == '6':
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.run()
