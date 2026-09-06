# Start with 3 pre-populated tasks
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

# Display the current to-do list
print("=" * 40)
print("          My To-Do List")
print("=" * 40)

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

print()
print(f"Total tasks: {len(tasks)}")

# Ask the user what they want to do
print()
print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

choice = input("Choice: ")

# Add a task using append()
if choice == "1":
    new_task = input("Enter new task: ")
    tasks.append(new_task)

# Remove a task using pop()
elif choice == "2":
    try:
        task_number = int(input("Enter task number to remove: "))

        # Convert the user's 1-based number to Python's 0-based index
        if task_number < 1 or task_number > len(tasks):
            raise IndexError

        removed_task = tasks.pop(task_number - 1)
        print(f"Removed: {removed_task}")

    # Handle invalid numbers or non-number input
    except (ValueError, IndexError):
        print("That's not a valid task number.")

# Display the updated list
print()
print("Updated list:")

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Show total number of tasks remaining
print()
print(f"Total tasks: {len(tasks)}")