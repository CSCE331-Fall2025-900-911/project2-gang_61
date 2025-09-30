import csv

members_data = [
    {"member_name": "Alice Smith", "contact_info": "alice@example.com", "reward_points": 1200},
    {"member_name": "Bob Johnson", "contact_info": "bob@example.com", "reward_points": 850},
    {"member_name": "Carol Lee", "contact_info": "carol@example.com", "reward_points": 1500},
    {"member_name": "David Kim", "contact_info": "david@example.com", "reward_points": 950},
    {"member_name": "Evelyn Turner", "contact_info": "evelyn@example.com", "reward_points": 1100},
    {"member_name": "Frank Harris", "contact_info": "frank@example.com", "reward_points": 780},
    {"member_name": "Grace Chen", "contact_info": "grace@example.com", "reward_points": 1340},
    {"member_name": "Henry Patel", "contact_info": "henry@example.com", "reward_points": 990},
    {"member_name": "Isabel Gomez", "contact_info": "isabel@example.com", "reward_points": 1230},
    {"member_name": "Jack Wilson", "contact_info": "jack@example.com", "reward_points": 870},
]

with open("members.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["member_id", "member_name", "contact_info", "reward_points"])
    writer.writeheader()
    for idx, member in enumerate(members_data, start=1):
        row = {
            "member_id": idx,
            "member_name": member["member_name"],
            "contact_info": member["contact_info"],
            "reward_points": member["reward_points"]
        }
        writer.writerow(row)

employees_data = [
    {"employee_name": "Sarah Miller", "role": "manager", "tips": 120.50},
    {"employee_name": "Tom Lee", "role": "cashier", "tips": 45.75},
    {"employee_name": "Emily Davis", "role": "cashier", "tips": 67.20},
    {"employee_name": "James Smith", "role": "manager", "tips": 98.00},
    {"employee_name": "Linda Brown", "role": "cashier", "tips": 53.10},
    {"employee_name": "Kevin White", "role": "cashier", "tips": 72.85},
    {"employee_name": "Olivia Green", "role": "manager", "tips": 110.40},
    {"employee_name": "Brian Clark", "role": "cashier", "tips": 60.00},
    {"employee_name": "Jessica Adams", "role": "cashier", "tips": 80.25},
    {"employee_name": "David Turner", "role": "manager", "tips": 105.90},
]

with open("employees.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["employee_id", "employee_name", "role", "tips"])
    writer.writeheader()
    for idx, employee in enumerate(employees_data, start=1):
        row = {
            "employee_id": idx,
            "employee_name": employee["employee_name"],
            "role": employee["role"],
            "tips": employee["tips"]
        }
        writer.writerow(row)

products_data = [
    # Drinks
    {"product_name": "Classic Milk Tea", "category": "Drink", "price": 4.50, "cost": 1.50, "stock": 120},
    {"product_name": "Taro Milk Tea", "category": "Drink", "price": 4.75, "cost": 1.60, "stock": 100},
    {"product_name": "Matcha Milk Tea", "category": "Drink", "price": 5.00, "cost": 1.80, "stock": 90},
    {"product_name": "Wintermelon Tea", "category": "Drink", "price": 4.25, "cost": 1.40, "stock": 80},
    {"product_name": "Thai Tea", "category": "Drink", "price": 4.75, "cost": 1.60, "stock": 85},
    {"product_name": "Strawberry Green Tea", "category": "Drink", "price": 4.50, "cost": 1.70, "stock": 70},
    {"product_name": "Honey Lemonade", "category": "Drink", "price": 4.00, "cost": 1.30, "stock": 60},
    {"product_name": "Brown Sugar Boba Milk", "category": "Drink", "price": 5.25, "cost": 2.00, "stock": 95},

    # Add-ons
    {"product_name": "Boba (Add-on)", "category": "Add-on", "price": 0.75, "cost": 0.20, "stock": 200},
    {"product_name": "Tapioka (Add-on)", "category": "Add-on", "price": 0.75, "cost": 0.20, "stock": 150},
    {"product_name": "Lychee Jelly (Add-on)", "category": "Add-on", "price": 0.75, "cost": 0.25, "stock": 130},
    {"product_name": "Aloe Vera (Add-on)", "category": "Add-on", "price": 0.75, "cost": 0.25, "stock": 100},
    {"product_name": "Red Bean (Add-on)", "category": "Add-on", "price": 0.75, "cost": 0.20, "stock": 80},

    # Toppings sold separately
    {"product_name": "Boba (Bowl)", "category": "Topping", "price": 2.00, "cost": 0.75, "stock": 30},
    {"product_name": "Tapioka (Bowl)", "category": "Topping", "price": 2.00, "cost": 0.75, "stock": 25},

    # Supplies
    {"product_name": "Large Cup", "category": "Supply", "price": 0.00, "cost": 0.10, "stock": 500},
    {"product_name": "Medium Cup", "category": "Supply", "price": 0.00, "cost": 0.08, "stock": 400},
    {"product_name": "Small Cup", "category": "Supply", "price": 0.00, "cost": 0.05, "stock": 300},
    {"product_name": "Straw", "category": "Supply", "price": 0.00, "cost": 0.02, "stock": 1000},
    {"product_name": "Sealing Film", "category": "Supply", "price": 0.00, "cost": 0.03, "stock": 800},

    # Merchandise
    {"product_name": "Sharetea Tote Bag", "category": "Merchandise", "price": 8.00, "cost": 4.50, "stock": 15},
    {"product_name": "Reusable Cup", "category": "Merchandise", "price": 10.00, "cost": 6.00, "stock": 20},
]

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["product_id", "product_name", "category", "price", "cost", "stock"])
    writer.writeheader()
    for idx, product in enumerate(products_data, start=1):
        row = {
            "product_id": idx,
            "product_name": product["product_name"],
            "category": product["category"],
            "price": product["price"],
            "cost" : product["cost"],
            "stock": product["stock"]
        }
        writer.writerow(row)

orders_data = [
    # Only "in progress" and "completed" orders, about 2 "in progress"
    {"member_id": 1, "employee_id": 2, "order_time": "4:55", "order_status": "in progress"},
    {"member_id": "", "employee_id": 4, "order_time": "2:22", "order_status": "in progress"},
    {"member_id": 7, "employee_id": 6, "order_time": "3:21", "order_status": "completed"},
    {"member_id": "", "employee_id": 1, "order_time": "2:15", "order_status": "completed"},
    {"member_id": 2, "employee_id": 9, "order_time": "2:47", "order_status": "completed"},
    {"member_id": 5, "employee_id": 8, "order_time": "4:05", "order_status": "completed"},
    {"member_id": "", "employee_id": 10, "order_time": "3:02", "order_status": "completed"},
    {"member_id": 4, "employee_id": 7, "order_time": "2:59", "order_status": "completed"},
]

with open("orders.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["order_id", "member_id", "employee_id", "order_time", "order_status"])
    writer.writeheader()
    for idx, order in enumerate(orders_data, start=1):
        row = {
            "order_id": idx,
            "member_id": order["member_id"],
            "employee_id": order["employee_id"],
            "order_time": order["order_time"],
            "order_status": order["order_status"]
        }
        writer.writerow(row)

#either requires another column or three p keys
items_data = [
    # Drink items (with sugar/ice levels and applicable supplies)
    {"item_id": 1, "order_id": 1, "product_id": 1, "price": 5.25, "sugar_level": "medium", "ice_level": "light"},  # Classic Milk Tea
    {"item_id": 1, "order_id": 1, "product_id": 9, "price": 5.25, "sugar_level": "medium", "ice_level": "light"},  # Boba (Add-on)
    {"item_id": 1, "order_id": 1, "product_id": 17, "price": 5.25, "sugar_level": "medium", "ice_level": "light"}, # Large Cup
    {"item_id": 1, "order_id": 1, "product_id": 20, "price": 5.25, "sugar_level": "medium", "ice_level": "light"}, # Straw
    {"item_id": 1, "order_id": 1, "product_id": 21, "price": 5.25, "sugar_level": "medium", "ice_level": "light"}, # Sealing Film

    {"item_id": 2, "order_id": 1, "product_id": 2, "price": 4.75, "sugar_level": "extra", "ice_level": "medium"},  # Taro Milk Tea
    {"item_id": 2, "order_id": 1, "product_id": 18, "price": 4.75, "sugar_level": "extra", "ice_level": "medium"}, # Medium Cup
    {"item_id": 2, "order_id": 1, "product_id": 20, "price": 4.75, "sugar_level": "extra", "ice_level": "medium"}, # Straw
    {"item_id": 2, "order_id": 1, "product_id": 21, "price": 4.75, "sugar_level": "extra", "ice_level": "medium"}, # Sealing Film

    {"item_id": 3, "order_id": 2, "product_id": 3, "price": 5.75, "sugar_level": "medium", "ice_level": "medium"}, # Matcha Milk Tea
    {"item_id": 3, "order_id": 2, "product_id": 10, "price": 5.75, "sugar_level": "medium", "ice_level": "medium"},# Tapioka (Add-on)
    {"item_id": 3, "order_id": 2, "product_id": 17, "price": 5.75, "sugar_level": "medium", "ice_level": "medium"},# Large Cup
    {"item_id": 3, "order_id": 2, "product_id": 20, "price": 5.75, "sugar_level": "medium", "ice_level": "medium"},# Straw
    {"item_id": 3, "order_id": 2, "product_id": 21, "price": 5.75, "sugar_level": "medium", "ice_level": "medium"},# Sealing Film

    {"item_id": 4, "order_id": 3, "product_id": 8, "price": 6.00, "sugar_level": "light", "ice_level": "extra"},   # Brown Sugar Boba Milk
    {"item_id": 4, "order_id": 3, "product_id": 9, "price": 6.00, "sugar_level": "light", "ice_level": "extra"},   # Boba (Add-on)
    {"item_id": 4, "order_id": 3, "product_id": 17, "price": 6.00, "sugar_level": "light", "ice_level": "extra"},  # Large Cup
    {"item_id": 4, "order_id": 3, "product_id": 20, "price": 6.00, "sugar_level": "light", "ice_level": "extra"},  # Straw
    {"item_id": 4, "order_id": 3, "product_id": 21, "price": 6.00, "sugar_level": "light", "ice_level": "extra"},  # Sealing Film

    {"item_id": 5, "order_id": 4, "product_id": 5, "price": 4.75, "sugar_level": "medium", "ice_level": "medium"}, # Thai Tea
    {"item_id": 5, "order_id": 4, "product_id": 18, "price": 4.75, "sugar_level": "medium", "ice_level": "medium"},# Medium Cup
    {"item_id": 5, "order_id": 4, "product_id": 20, "price": 4.75, "sugar_level": "medium", "ice_level": "medium"},# Straw
    {"item_id": 5, "order_id": 4, "product_id": 21, "price": 4.75, "sugar_level": "medium", "ice_level": "medium"},# Sealing Film

    {"item_id": 6, "order_id": 5, "product_id": 6, "price": 5.25, "sugar_level": "extra", "ice_level": "light"},   # Strawberry Green Tea
    {"item_id": 6, "order_id": 5, "product_id": 11, "price": 5.25, "sugar_level": "extra", "ice_level": "light"},  # Lychee Jelly (Add-on)
    {"item_id": 6, "order_id": 5, "product_id": 17, "price": 5.25, "sugar_level": "extra", "ice_level": "light"},  # Large Cup
    {"item_id": 6, "order_id": 5, "product_id": 20, "price": 5.25, "sugar_level": "extra", "ice_level": "light"},  # Straw
    {"item_id": 6, "order_id": 5, "product_id": 21, "price": 5.25, "sugar_level": "extra", "ice_level": "light"},  # Sealing Film

    {"item_id": 7, "order_id": 6, "product_id": 4, "price": 4.25, "sugar_level": "medium", "ice_level": "medium"}, # Wintermelon Tea
    {"item_id": 7, "order_id": 6, "product_id": 18, "price": 4.25, "sugar_level": "medium", "ice_level": "medium"},# Medium Cup
    {"item_id": 7, "order_id": 6, "product_id": 20, "price": 4.25, "sugar_level": "medium", "ice_level": "medium"},# Straw
    {"item_id": 7, "order_id": 6, "product_id": 21, "price": 4.25, "sugar_level": "medium", "ice_level": "medium"},# Sealing Film

    {"item_id": 8, "order_id": 7, "product_id": 7, "price": 4.00, "sugar_level": "light", "ice_level": "medium"},  # Honey Lemonade
    {"item_id": 8, "order_id": 7, "product_id": 19, "price": 4.00, "sugar_level": "light", "ice_level": "medium"}, # Small Cup
    {"item_id": 8, "order_id": 7, "product_id": 20, "price": 4.00, "sugar_level": "light", "ice_level": "medium"}, # Straw
    {"item_id": 8, "order_id": 7, "product_id": 21, "price": 4.00, "sugar_level": "light", "ice_level": "medium"}, # Sealing Film

    {"item_id": 9, "order_id": 8, "product_id": 1, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"},  # Classic Milk Tea
    {"item_id": 9, "order_id": 8, "product_id": 9, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"},  # Boba (Add-on)
    {"item_id": 9, "order_id": 8, "product_id": 10, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"}, # Tapioka (Add-on)
    {"item_id": 9, "order_id": 8, "product_id": 17, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"}, # Large Cup
    {"item_id": 9, "order_id": 8, "product_id": 20, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"}, # Straw
    {"item_id": 9, "order_id": 8, "product_id": 21, "price": 6.00, "sugar_level": "medium", "ice_level": "extra"}, # Sealing Film

    # Non-drink items (no sugar/ice levels)
    {"item_id": 10, "order_id": 7, "product_id": 22, "price": 8.00, "sugar_level": "", "ice_level": ""},           # Sharetea Tote Bag
    {"item_id": 11, "order_id": 8, "product_id": 23, "price": 10.00, "sugar_level": "", "ice_level": ""},          # Reusable Cup

    # Snack items
    {"item_id": 12, "order_id": 1, "product_id": 15, "price": 2.00, "sugar_level": "", "ice_level": ""},           # Boba (Bowl)
    {"item_id": 13, "order_id": 2, "product_id": 16, "price": 2.00, "sugar_level": "", "ice_level": ""},           # Tapioka (Bowl)
]

with open("items.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["item_id", "order_id", "product_id", "price", "sugar_level", "ice_level"])
    writer.writeheader()
    for item in items_data:
        row = {
            "item_id": item["item_id"],
            "order_id": item["order_id"],
            "product_id": item["product_id"],
            "price": item["price"],
            "sugar_level": item["sugar_level"],
            "ice_level": item["ice_level"]
        }
        writer.writerow(row)



