# generate_members.py
import csv
from faker import Faker

fake = Faker()

with open("members.csv", mode="w", newline="", encoding="utf-8") as f:
    fieldnames = ["member_id", "member_name", "contact_info", "reward_points"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for member_id in range(1, 501):
        writer.writerow({
            "member_id": member_id,
            "member_name": fake.name(),
            "contact_info": fake.email(),
            "reward_points": fake.random_int(min=0, max=500)
        })
