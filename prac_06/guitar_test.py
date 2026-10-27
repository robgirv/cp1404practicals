"""
CP1404 Prac 06 – Guitars!
See `guitar.py` for timing info.
"""
from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(f"Expect: 104 | Got: {gibson_guitar.get_age()}")

print(f"Is vintage? Expect True | Got: {gibson_guitar.is_vintage()}")
