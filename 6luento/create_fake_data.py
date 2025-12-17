import csv
import random

# Tiedoston nimi
csv_file = "./input.csv"

# Sarakkeet
fields = ['id', 'name', 'amount']

# Lista esimerkkinimiä
first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Wilson"]

# Luo 2000 henkilöä
rows = []
for i in range(1, 2000000):
    person_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    amount = random.randint(50, 1000)
    rows.append({'id': i, 'name': person_name, 'amount': amount})

# Kirjoitetaan CSV-tiedostoon
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

csv_file
