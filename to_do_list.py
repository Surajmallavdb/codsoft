# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

    def update_task(self, task_number, task):
        try:
            self.tasks[task_number - 1]["task"] = task
        except IndexError:
            print("Invalid task number")

    def mark_done(self, task_number):
        try:
            self.tasks[task_number - 1]["done"] = True
        except IndexError:
            print("Invalid task number")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            task = input("Enter the updated task: ")
            todo.update_task(task_number, task)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as done: "))
            todo.mark_done(task_number)
        elif choice == "5":
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()