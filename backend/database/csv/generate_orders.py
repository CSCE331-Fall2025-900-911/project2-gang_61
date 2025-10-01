import csv
import random
from datetime import datetime, timedelta

weeks = 39
orders_per_week = 19000  # ~750k sales total
business_start_hour = 11
business_end_hour = 22

# 15 random peak days spread across the 39 weeks
peak_days = []
weeks_sampled = random.sample(range(weeks), 15)
for week in weeks_sampled:
    start_date = datetime.now() - timedelta(weeks=(weeks - week))
    peak_day = start_date + timedelta(days=random.randint(0, 6))
    peak_days.append(peak_day.date())

with open("orders.csv", mode="w", newline="", encoding="utf-8") as f:
    fieldnames = ["order_id", "member_id", "employee_id", "order_time", "order_status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    order_id = 1
    for week in range(weeks):
        start_date = datetime.now() - timedelta(weeks=(weeks - week))
        for _ in range(orders_per_week):
            order_date = start_date + timedelta(
                days=random.randint(0, 6),
                hours=random.randint(business_start_hour, business_end_hour),
                minutes=random.randint(0, 59)
            )

            # if this day is a peak day, then increase volume
            multiplier = 3 if order_date.date() in peak_days else 1
            for _ in range(multiplier):
                random_num = random.randint(1, 100)
                if random_num <= 40:
                    member_id = random.randint(1, 500)
                else:
                    member_id = 0
                writer.writerow({
                    "order_id": order_id,
                    "member_id": member_id,
                    "employee_id": random.randint(1, 50),
                    "order_time": order_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "order_status": random.choice(["Completed"]*3 + ["Cancelled"])
                })
                order_id += 1
