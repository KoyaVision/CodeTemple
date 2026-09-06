# Ask the user for trip information
destination = input("Enter your destination: ")
distance = float(input("Enter total distance in miles: "))
mpg = float(input("Enter your car's miles per gallon: "))
gas_price = float(input("Enter the current gas price per gallon: "))
nights = int(input("Enter the number of nights you will stay: "))
hotel_cost = float(input("Enter the average hotel cost per night: "))
food_budget = float(input("Enter your daily food budget: "))

# Calculate trip costs
gallons_needed = distance / mpg
gas_cost = gallons_needed * gas_price
total_hotel_cost = nights * hotel_cost
total_food_cost = (nights + 1) * food_budget
grand_total = gas_cost + total_hotel_cost + total_food_cost

# Display the trip summary
print()
print("=== Road Trip Budget Planner ===")
print()
print(f"Destination: {destination}")
print(f"Distance: {distance:.2f} miles")
print()
print("--- Cost Breakdown ---")
print(f"Gas ({gallons_needed:.2f} gal @ ${gas_price:.2f}/gal): ${gas_cost:.2f}")
print(f"Hotel ({nights} nights @ ${hotel_cost:.2f}): ${total_hotel_cost:.2f}")
print(f"Food ({nights + 1} days @ ${food_budget:.2f}): ${total_food_cost:.2f}")
print("------------------------------")
print(f"Estimated Total: ${grand_total:.2f}")