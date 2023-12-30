import os
import pickle

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def save_to_file(self, filename="todolist.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename="todolist.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Save To-Do List")
        print("5. Load To-Do List")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.save_to_file()
            print("To-Do List saved successfully.")
        elif choice == "5":
            todo_list.load_from_file()
            print("To-Do List loaded successfully.")
        elif choice == "6":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
