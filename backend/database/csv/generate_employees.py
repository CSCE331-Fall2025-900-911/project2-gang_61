# generate_employees.py
import csv
import random
from faker import Faker

fake = Faker()

roles = ["manager", "cashier"] 


headers = ["employee_id", "employee_name", "role", "tips"]

# Generate 50 employees
employees = []
for i in range(1, 51):
    employee_name = fake.first_name()
    email = f"{employee_name.lower()}.@example.com"
    role = random.choice(roles)
    tips = random.randint(1, 500)

    employees.append([i, employee_name, role, tips])

# Write to CSV
with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(employees)

