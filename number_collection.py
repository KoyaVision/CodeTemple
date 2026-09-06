# Snippet 1
# Prediction: TypeError because Python cannot concatenate a string and an integer

# Snippet 2
# Prediction: TypeError because input() returns a string and a string cannot be added to an integer

# Snippet 3
# Prediction: SyntaxError because the string is missing its closing quotation mark

# Snippet 4
# Prediction: ValueError because "twenty-five" cannot be converted to an integer

# Snippet 5
# Prediction: NameError because username has not been defined

# Get the first number
try:
    number1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number1 = 0

# Get the second number
try:
    number2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number2 = 0

# Get the third number
try:
    number3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number3 = 0

# Calculate the sum and average
total = number1 + number2 + number3
average = total / 3

# Display the results
print()
print(f"Your numbers: {number1}, {number2}, {number3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")