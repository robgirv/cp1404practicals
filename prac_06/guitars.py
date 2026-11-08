"""
CP1404 Prac 06 – Guitars!
See `guitar.py` for timing info.
"""
from guitar import Guitar
from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")

print("\n... snip ...\n")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""

    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
