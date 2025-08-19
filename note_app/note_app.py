file_name = input("Enter file name: ").strip()


# Check user input file name ends with '.txt' otherwise quit
if not file_name.endswith(".txt"):
    print("⚠️ Your file name should end with '.txt'")
    quit()

while True:
    try:
        command = input("Enter command (write/read/stop): ").lower().strip()

        if command == "stop":
            print("👋 Goodbye!")
            break

        elif command == "write":
            note = input("Write a note: ").strip()
            with open(file_name, "a") as f:
                f.write(note + "\n")
            print("✅ Note saved!")

        elif command == "read":
            with open(file_name, "r") as f:
                content = f.read()
            print("\n📄 File content:\n")
            print(content if content else "⚠️ File is empty.")

        else:
            print("⚠️ Invalid command! Please use 'write', 'read', or 'stop'.")

    except FileNotFoundError:
        print("⚠️ File not found, please check the name!")

    finally:
        print("✅ Operation complete.")
