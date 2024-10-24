command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print(f"Executing command: {command}")
    command = input("Enter command: ")
else:
    print("Goodbye!")
print("Execution stopped.")
