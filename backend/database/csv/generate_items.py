import csv
import random


with open("orders.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    orders = [row for row in reader]


ORDERS_START = 1
ORDERS_END = len(orders)    


# product ID ranges                ID:
DRINKS = list(range(1, 10))       # 1–9
TOPPINGS = list(range(10, 15))    # 10–14
BOWLS = list(range(15, 17))       # 15–16
CUPS = list(range(17, 20))        # 17–19
STRAW = 20                        # always include
MERCH = [22, 23]                  # optional extras


products = {}
with open("products.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products[int(row["product_id"])] = {
            "product_id": int(row["product_id"]),
            "product_name": row["product_name"],
            "category": row["category"],
            "price": float(row["price"]),
            "cost": float(row["cost"]),
            "stock": int(row["stock"])
        }

   

items_data = []
item_id = 1
group_id = 1  # this will group the items together (e.g. boba milk tea where boba is included in drink)

# We assume that each customer will buy at least one drink

for order_id in range(ORDERS_START, ORDERS_END + 1):
    num_drinks = random.randint(1, 3)

    for _ in range(num_drinks):
        # Each drink combo is one group
        current_group = group_id
        group_id += 1

        # Required drink
        drink_id = random.choice(DRINKS)
        sugar_level = random.choice(["none", "light", "medium", "extra"])
        ice_level = random.choice(["none", "light", "medium", "extra"])
        items_data.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": drink_id,
            "price": products[drink_id]["price"],
            "sugar_level": sugar_level,
            "ice_level": ice_level,
            "group_id": current_group
        })
        item_id += 1

        # Required cup
        cup_id = random.choice(CUPS)
        items_data.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": cup_id,
            "price": products[cup_id]["price"],
            "sugar_level": "",
            "ice_level": "",
            "group_id": current_group
        })
        item_id += 1

        # Required straw
        items_data.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": STRAW,
            "price": products[STRAW]["price"],
            "sugar_level": "",
            "ice_level": "",
            "group_id": current_group
        })
        item_id += 1

        # Optional topping
        if random.random() < 0.3:  # 30% chance
            topping_id = random.choice(TOPPINGS)
            items_data.append({
                "item_id": item_id,
                "order_id": order_id,
                "product_id": topping_id,
                "price": products[topping_id]["price"],
                "sugar_level": "",
                "ice_level": "",
                "group_id": current_group
            })
            item_id += 1

        # Optional boba bowl
        if random.random() < 0.1:  # 10% chance
            bowl_id = random.choice(BOWLS)
            items_data.append({
                "item_id": item_id,
                "order_id": order_id,
                "product_id": bowl_id,
                "price": products[bowl_id]["price"],
                "sugar_level": "",
                "ice_level": "",
                "group_id": current_group
            })
            item_id += 1

    # Optional merchandise (separate group from drinks)
    if random.random() < 0.05:  # 5% chance
        merch_id = random.choice(MERCH)
        current_group = group_id
        group_id += 1
        items_data.append({
            "item_id": item_id,
            "order_id": order_id,
            "product_id": merch_id,
            "price": products[merch_id]["price"],
            "sugar_level": "",
            "ice_level": "",
            "group_id": current_group
        })
        item_id += 1

# Write items.csv
with open("items.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["item_id", "order_id", "product_id", "price", "sugar_level", "ice_level", "group_id"]
    )
    writer.writeheader()
    writer.writerows(items_data)
