📝 Notes App

A simple command-line Notes App built with Python to practice error
handling (try/except/finally) and file operations.

------------------------------------------------------------------------

🚀 Features

-   Save notes into a .txt file
-   Read saved notes
-   Exit anytime with stop
-   Handles errors gracefully with try/except

------------------------------------------------------------------------

⚙️ How It Works

1.  App asks for a filename (must end with .txt)
2.  User chooses a command:
    -   write → add a note to the file
    -   read → show all notes in the file
    -   stop → exit the program

------------------------------------------------------------------------

▶️ Run the App

Clone the repo and navigate to the project folder:

    git clone https://github.com/Makhmud-egp/python-practice.git
    cd python-practice/notes_app

Run the script:

    python notes_app.py

------------------------------------------------------------------------

💡 Example

    Enter file name: my_notes.txt
    Enter command (write/read/stop): write
    Write a note: Learn Python
    ✅ Note saved!
    ✅ Operation complete.

    Enter command (write/read/stop): read

    📄 File content:
    Learn Python
    ✅ Operation complete.

    Enter command (write/read/stop): stop
    👋 Goodbye!

------------------------------------------------------------------------

📚 Learning Points

-   try/except → catches file not found errors
-   finally → always runs cleanup code
-   endswith(“.txt”) → ensures correct file format
-   while loop → keeps app running until stop

Mnemonic: “NAME → ACTION → CATCH → CLEANUP”
- NAME the file
- ACTION (write/read/stop)
- CATCH errors
- CLEANUP with finally
