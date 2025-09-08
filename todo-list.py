def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

tasks = []

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added.")
    elif choice == "2":
        print("\n📋 Your Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{removed}' removed.")
        else:
            print("❌ Invalid task number.")
    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, try again.")
