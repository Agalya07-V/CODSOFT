tasks = []  

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    name = input("Enter task: ")
    tasks.append({"task": name, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            status = "Done" if t["done"] else "NOT Done"
            print(f"{i + 1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid number.")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: ")) - 1
    if 0 <= num < len(tasks):
        removed = tasks.pop(num)
        print(f"Task '{removed['task']}' deleted!")
    else:
        print("Invalid number.")


while True:
    show_menu()
    choice = input("Enter a option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("The To-Do List will End")
        break
    else:
        print("INVALID option,Please Enter a valid option.")
