inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "monitor": {"price": 100.00, "quantity": 50},
    "keyboard": {"price": 30.00, "quantity": 50},
}

# Display the full inventory
print("=" * 50)
print("                 STORE INVENTORY")
print("=" * 50)
print(f"{'Product':<12}{'Price':<12}{'Quantity':<10}")
print("-" * 50)

for product, details in inventory.items():
    print(f"{product:<12}${details['price']:<11.2f}{details['quantity']:<10}")

# Calculate total inventory value
total_value = 0

for product, details in inventory.items():
    total_value += details["price"] * details["quantity"]

print("-" * 50)
print(f"Total Inventory Value: ${total_value:.2f}")

# Let the user look up a product using .get()
print()
search_product = input("Enter a product to look up: ").lower()

product_details = inventory.get(search_product)

if product_details:
    print(f"Product: {search_product}")
    print(f"Price: ${product_details['price']:.2f}")
    print(f"Quantity: {product_details['quantity']}")
else:
    print("Product not found.")

# Let the user update a product quantity
print()
update_product = input("Enter a product to update: ").lower()

product_details = inventory.get(update_product)

if product_details:
    try:
        new_quantity = int(input("Enter the new quantity: "))
        product_details["quantity"] = new_quantity
        print(f"{update_product} quantity updated to {new_quantity}.")
    except ValueError:
        print("Invalid quantity.")
else:
    print("Product not found.")

# Use a set to track low-stock products
low_stock = set()

for product, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(product)

# Display low-stock alert
print()
print("=" * 50)
print("LOW STOCK ALERT")
print("=" * 50)

if low_stock:
    for product in low_stock:
        print(f"{product} needs restocking.")
else:
    print("No products are currently low on stock.")