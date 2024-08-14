class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

    def mark_as_completed(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
        except IndexError:
            print("Invalid task number.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']} - {'Completed' if task['completed'] else 'Not Completed'}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    task, status = line.strip().split(" - ")
                    self.tasks.append({"task": task, "completed": status == "Completed"})
        except FileNotFoundError:
            print("File not found.")
todo_list = ToDoList()
while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark as Completed")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        task_number = int(input("Enter task number to delete: "))
        todo_list.delete_task(task_number)
    elif choice == "4":
        task_number = int(input("Enter task number to mark as completed: "))
        todo_list.mark_as_completed(task_number)
    elif choice == "5":
        filename = input("Enter filename to save: ")
        todo_list.save_to_file(filename)
    elif choice == "6":
        filename = input("Enter filename to load: ")
        todo_list.load_from_file(filename)
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")