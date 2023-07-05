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
        if not self.tasks:
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
        task_number = self.get_task_number("Enter the task number to edit: ")
        if task_number is not None:
            new_description = input("Enter the new task description: ")
            self.tasks[task_number]["description"] = new_description
            print("Task edited successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        task_number = self.get_task_number("Enter the task number to delete: ")
        if task_number is not None:
            del self.tasks[task_number]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self):
        self.view_tasks()
        task_number = self.get_task_number("Enter the task number to mark as completed: ")
        if task_number is not None:
            self.tasks[task_number]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def get_task_number(self, prompt):
        task_count = len(self.tasks)
        if task_count == 0:
            return None
        while True:
            task_number = input(prompt)
            if task_number.isdigit():
                task_number = int(task_number)
                if 1 <= task_number <= task_count:
                    return task_number - 1
            print("Invalid task number. Please try again.")

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
