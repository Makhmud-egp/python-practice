# 📊 Expense Tracker v2

A simple **command-line Expense Tracker** built with Python.  
It allows you to **add expenses, view all expenses, calculate totals, and export data to JSON**.

---

## 📂 Project Structure

expense_tracker_v2/
│
├── expense_tracker_v2.py # Main script
├── expenses.json # Saved expenses (auto-created)
└── README.md # Documentation



---

## ⚡ Features

- ➕ Add a new expense (amount + category + description)  
- 📋 View all saved expenses  
- 💰 Calculate total expenses  
- 💾 Save and load data from JSON file  
- ✅ Simple command-line interface  

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Makhmud-egp/python-practice.git
   cd python-practice/expense_tracker_v2

2. Run the script:
   ```bash
   python expense_tracker_v2.py


## 💡 Example Usage

Enter a command (add/show/total/stop): add
Enter amount: 15
Enter category: Food
Enter description: Lunch

✅ Expense added successfully!

Enter a command (add/show/total/stop): show
1. $15 - Food (Lunch)

Enter a command (add/show/total/stop): total
💰 Total Expenses: $15

Enter a command (add/show/total/stop): stop
Goodbye!
