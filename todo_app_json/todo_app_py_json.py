import json
import os

FILE_NAME = "ToDo.json"

def load_data():
    """Load tasks from JSON file."""
    if not os.path.isfile(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

while True:
    command = input("Enter a command (add/show/done/stop): ").lower().strip()

    if command == "stop":
        print("👋 Goodbye!")
        break

    elif command == "add":
        task = input("Enter a task: ").strip()
        if not task:
            print("❌ Task cannot be empty.")
            continue

        data = load_data()
        data.append({"ToDo": task})
        save_data(data)
        print(f"✅ Task '{task}' added!")

    elif command == "show":
        data = load_data()
        if not data:
            print("📭 No tasks found.")
        else:
            print("\n📝 Your To-Do List:")
            for i, item in enumerate(data, start=1):
                print(f"{i:<3} {item['ToDo']}")
            print("-" * 30)

    elif command == "done":
        data = load_data()
        if not data:
            print("📭 No tasks found.")
        else:
            for i, item in enumerate(data, start=1):
                print(f"{i}. {item['ToDo']}")

            num = input("Enter the number of the task to mark as done: ").strip()
            if num.isdigit() and 1 <= int(num) <= len(data):
                removed_task = data.pop(int(num) - 1)
                save_data(data)
                print(f"✅ Task '{removed_task['ToDo']}' marked as done.")
            else:
                print("❌ Invalid task number.")

    else:
        print("❌ Invalid command. Please use 'add', 'show', 'done', or 'stop'.")
