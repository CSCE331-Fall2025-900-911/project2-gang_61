# generate_orders.py
import csv
import random
from datetime import datetime, timedelta

weeks = 39
orders_per_week = 19000  # ~750k sales total
peak_day = datetime.now() - timedelta(weeks=5)  # 1 peak ~5 weeks ago 

with open("orders.csv", mode="w", newline="", encoding="utf-8") as f:
    fieldnames = ["order_id", "member_id", "employee_id", "order_time", "order_status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    order_id = 1
    for week in range(weeks):
        start_date = datetime.now() - timedelta(weeks=(weeks - week))
        for _ in range(orders_per_week):
            # random day + time in the week
            order_date = start_date + timedelta(days=random.randint(0, 6),
                                                hours=random.randint(8, 21),
                                                minutes=random.randint(0, 59))

            # peak day boost
            if order_date.date() == peak_day.date():
                for _ in range(3):  # triple orders on peak day
                    writer.writerow({
                        "order_id": order_id,
                        "member_id": random.randint(1, 500),  # 500 members
                        "employee_id": random.randint(1, 50),  # 50 employees
                        "order_time": order_date.strftime("%Y-%m-%d %H:%M:%S"),
                        "order_status": random.choice(["Completed", "Completed", "Completed", "Cancelled"])
                    })
                    order_id += 1
            else:
                writer.writerow({
                    "order_id": order_id,
                    "member_id": random.randint(1, 500),
                    "employee_id": random.randint(1, 50),
                    "order_time": order_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "order_status": random.choice(["Completed", "Completed", "Completed", "Cancelled"])
                })
                order_id += 1
