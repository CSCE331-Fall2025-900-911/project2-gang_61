import csv
import random

# Read products from CSV
products = []
with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append({
            "product_id": int(row["product_id"]),
            "product_name": row["product_name"],
            "category": row["category"],
            "price": float(row["price"]),
            "cost" : float(row["cost"]),
            "stock" : int(row["stock"])
        })

# Generate items for orders
items_data = []
for item_id in range(1, 1001):  # 1000 items
    order_id = random.randint(1, 4000)  # random order
    product = random.choice(products)
    sugar_level = random.choice(["none", "light", "medium", "extra"]) if product["category"] == "Drink" else ""
    ice_level = random.choice(["none", "light", "medium", "extra"]) if product["category"] == "Drink" else ""
    
    items_data.append({
        "item_id": item_id,
        "order_id": order_id,
        "product_id": product["product_id"],
        "price": product["price"],
        "sugar_level": sugar_level,
        "ice_level": ice_level
    })

# Write items.csv
with open("items.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["item_id", "order_id", "product_id", "price", "sugar_level", "ice_level"])
    writer.writeheader()
    for item in items_data:
        writer.writerow(item)
