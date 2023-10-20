import pickle
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
def display(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. Title: {task.title}, Description: {task.description}, Status: {status}")
def save(tasks, filename):
    with open(filename, 'wb') as file:
        pickle.dump(tasks, file)
    print(f"Tasks saved to '{filename}'")
def load(filename):
    try:
        with open(filename, 'rb') as file:
            tasks = pickle.load(file)
        return tasks
    except FileNotFoundError:
        return []
def main():
    tasks = []
    filename = "tasks.txt"
    tasks = load(filename)
    while True:
        print("\nTask Management System")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to a file")
        print("6. Load tasks from a file")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            task = Task(title, description)
            tasks.append(task)
            print("Task added successfully!")
        elif choice == '2':
            display(tasks)
        elif choice == '3':
            display(tasks)
            try:
                index = int(input("Enter the index of the task to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index].completed = True
                    print("Task marked as completed.")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '4':
            display(tasks)
            try:
                index = int(input("Enter the index of the task to delete: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    print("Task deleted successfully.")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '5':
            save(tasks, filename)
        elif choice == '6':
            tasks = load(filename)
            print("Tasks loaded successfully!")
        elif choice == '7':
            save(tasks, filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")
if __name__ == "__main__":
    main()