# fragile_calc.py — Crashes on bad input
bill = float(input("Enter the bill amount: $"))
tip_rate = float(input("Enter tip percentage (e.g., 20): "))

tip = bill * (tip_rate / 100)
total = bill + tip

print(f"\\nTip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print()
# robust_calc.py — Handles bad input gracefully

print("=" * 30)
print("    Tip Calculator")
print("=" * 30)

# Get bill amount with error handling
try:
    bill = float(input("\\nEnter the bill amount: $"))
except ValueError:
    print("\\nError: Please enter a number (e.g., 45.99)")
    print("Exiting program.")
    exit()  # Stop the program cleanly

# Get tip percentage with error handling
try:
    tip_rate = float(input("Enter tip percentage (e.g., 20): "))
except ValueError:
    print("\\nError: Please enter a number (e.g., 20)")
    print("Exiting program.")
    exit()

# Calculate (safe because we know both are numbers now)
tip = bill * (tip_rate / 100)
total = bill + tip

# Display
print(f"\\nBill:  ${bill:.2f}")
print(f"Tip ({tip_rate:.0f}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
print()
# Even more robust version
try:
    bill = float(input("\\nEnter the bill amount: $"))
    if bill < 0:
        print("Error: Bill amount can't be negative.")
        exit()
    if bill == 0:
        print("Nothing to tip on!")
        exit()
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

try:
    tip_rate = float(input("Enter tip percentage (e.g., 20): "))
    if tip_rate < 0:
        print("Error: Tip percentage can't be negative.")
        exit()
    if tip_rate > 100:
        print(f"Wow, {tip_rate:.0f}% is very generous!")
        # Not an error — just a comment. Program continues.
except ValueError:
    print("Error: Please enter a valid number.")
    exit()