# My first Python program
# This prints a personal introduction

print("=" * 40)  # Prints a line of 40 equal signs
print("Personal Introduction")
print("=" * 40)

first_name = "Koya"
last_name = "A"
age = 33
city = "Houston"
favorite_language = "Python"  # Because we're learning it right now!
print("Name:", first_name, last_name)
print("Age:", age)
print("City:", city)
print("Favorite Language:", favorite_language)
print("=" * 40)
# f-strings let you embed variables directly in text
print(f"\n{first_name} is {age} years old and lives in {city}.")
print(f"They are learning {favorite_language} to build AI systems.")