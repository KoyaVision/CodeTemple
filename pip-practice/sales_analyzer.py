import csv


# Read sales data from CSV
sales = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales.append(row)


# Calculate totals
total_revenue = 0
product_revenue = {}
product_quantity = {}
daily_revenue = {}

for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    price = sale["price"]
    date = sale["date"]

    revenue = quantity * price
    total_revenue += revenue

    # Revenue per product
    if product not in product_revenue:
        product_revenue[product] = 0

    product_revenue[product] += revenue

    # Quantity sold per product
    if product not in product_quantity:
        product_quantity[product] = 0

    product_quantity[product] += quantity

    # Revenue per day
    if date not in daily_revenue:
        daily_revenue[date] = 0

    daily_revenue[date] += revenue


# Find the day with the highest total revenue
highest_revenue_day = None
highest_daily_revenue = 0

for date, revenue in daily_revenue.items():
    if revenue > highest_daily_revenue:
        highest_daily_revenue = revenue
        highest_revenue_day = date


# Write formatted text report
with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Revenue: ${total_revenue:.2f}\n")
    file.write(
        f"Highest Revenue Day: {highest_revenue_day} "
        f"(${highest_daily_revenue:.2f})\n\n"
    )

    file.write("BY PRODUCT:\n")

    for product in product_revenue:
        file.write(
            f"{product}: "
            f"{product_quantity[product]} units sold, "
            f"${product_revenue[product]:.2f} revenue\n"
        )


# Write product summary CSV
with open("product_summary.csv", "w", newline="") as file:
    fieldnames = ["product", "total_quantity", "total_revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for product in product_revenue:
        writer.writerow({
            "product": product,
            "total_quantity": product_quantity[product],
            "total_revenue": f"{product_revenue[product]:.2f}"
        })


print("Sales analysis complete.")
print("sales_report.txt created.")
print("product_summary.csv created.")