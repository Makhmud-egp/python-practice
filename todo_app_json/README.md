
# todo_app_python_json
=======
# 📝 ToDo List App (Python + JSON)

## 📌 Project Description
A simple **command-line To-Do List App** written in Python.  
Tasks are stored in a `ToDo.json` file so your list **persists even after closing** the program.  

---

## ⚙️ Features
- ➕ **Add** new tasks  
- 📋 **Show** all tasks  
- ✅ **Mark tasks as done** (removes them)  
- 🛑 **Stop** the program safely  
- 💾 **Saves automatically** to `ToDo.json`  

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Makhmud-egp/todo_app_python_json.git
cd todo_app_python_json

python todo_app_py_json.py

add   → Add a new task
show  → Show all tasks
done  → Mark task as done
stop  → Exit program


todo_app/
│── todo.py        # main program
│── ToDo.json      # tasks stored here (auto-created)
└── README.md      # project documentation



Enter a command (add/show/done/stop): add
Enter a task: Learn Python
✅ Task 'Learn Python' added!

Enter a command (add/show/done/stop): show
📝 Your To-Do List:
1   Learn Python
------------------------------

Enter a command (add/show/done/stop): done
1. Learn Python
Enter the number of the task to mark as done: 1
✅ Task 'Learn Python' marked as done.

Enter a command (add/show/done/stop): stop
Goodbye!




