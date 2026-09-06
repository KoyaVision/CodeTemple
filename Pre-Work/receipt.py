# Store the original data as strings
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"  # 7.5% sales tax

# Convert prices and tax rate from strings to floats
item1_price = float(item1_price)
item2_price = float(item2_price)
item3_price = float(item3_price)
tax_rate = float(tax_rate)

# Convert quantities from strings to integers
item1_qty = int(item1_qty)
item2_qty = int(item2_qty)
item3_qty = int(item3_qty)

# Calculate each item's line total
item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

# Calculate subtotal, tax, and grand total
subtotal = item1_total + item2_total + item3_total
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

divider = "=" * 40
line = "-" * 40

print(divider)
print("STORE RECEIPT")
print(divider)

print(f"{item1_name:<12} ${item1_price:.2f} x {item1_qty}    ${item1_total:.2f}")
print(f"{item2_name:<12} ${item2_price:.2f} x {item2_qty}    ${item2_total:.2f}")
print(f"{item3_name:<12} ${item3_price:.2f} x {item3_qty}   ${item3_total:.2f}")

print(line)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7.5%): ${tax_amount:.2f}")

print(divider)
print(f"TOTAL: ${grand_total:.2f}")
print(divider)