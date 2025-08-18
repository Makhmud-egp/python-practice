import json
import os

FILE_NAME = "expanses.json"

def load_data():
    """Load list of expanses from JSON. If missing or corrupted, return []"""
    if not os.path.isfile(FILE_NAME) or os.stat(FILE_NAME).st_size == 0:
        return []
        
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("⚠️ Data format was not a list. Starting fresh.")
                return []
            return data
    except json.JSONDecodeError:
        print("⚠️ JSON file looks corrupted. Starting fresh.")
        save_data([])
        return []
    except OSError as e:
        print(f"⚠️ Could not read file: {e}. Starting with empty list.")
        return []

def save_data(data):
    """Save list of expanses to JSON, with basic error handling."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    except OSError as e:
        print(f"⚠️ Could not write file: {e}. Your latest changes may not be saved.")

def get_positive_amount(prompt="Enter amount: "):
    """Keep asking until user gives a positive number"""
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("❌ Please enter a positive number.")
                continue
            return round(amount, 2)
        except ValueError:
            print("❌ Numbers only, e.g., 12 or 12.50")

def show_expenses(data):
    if not data:
        print("📭 No expenses found.")
        return
    print("\n📋 Expenses:")
    for i, item in enumerate(data, start=1):
        print(f"{i:>2}. {item['name']} — ${item['amount']:.2f}")
    print("-" * 32)


def main():
    while True:
        command = input("\nEnter command (add/show/delete/total/stop): ").lower().strip()

        if command == "stop":
            print("👋 Goodbye!")
            break

        elif command == "add":
            name = input("Enter expanse name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            amount = get_positive_amount("Enter amount: ")
            data = load_data()
            data.append({"name": name, "amount":amount})
            save_data(data)
            print(f"✅ Added {name} — ${amount:.2f}")

        elif command == "show":
            data = load_data()
            show_expenses(data)
        
        elif command == "delete":
            data = load_data()
            if not data:
                print("📭 No expenses to delete.")
                continue
            show_expenses(data)
            num = input("Enter number to delete: ").strip()
            if not num.isdigit():
                print("❌ Please enter a valid number.")
                continue
            idx = int(num)
            if 1 <= idx <= len(data):
                removed = data.pop(idx - 1)
                save_data(data)
                print(f"🗑️ Deleted {removed['name']} — ${removed['amount']:.2f}")
            else:
                print("❌ Number out of range.")
        
        elif command == "total":
            data = load_data()
            total = sum(item["amount"] for item in data)
            print(f"💵 Total: ${total:.2f}")
        
        else:
            print("❌ Invalid command. Use: add, show, delete, total, stop.")

if __name__ == "__main__":
    main()