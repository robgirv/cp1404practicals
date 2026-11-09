"""?"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """?"""
    guitars = store_guitars(FILENAME)

    print("Guitars (unsorted):")
    display_guitars(guitars)

    print("")

    print("Guitars (sorted):")
    display_guitars(sort_guitars(guitars))


def store_guitars(filename) -> list:
    """Store guitar data into list from CSV file."""
    guitars = []
    with open(filename) as in_file:
        in_file.readline()  # Skip CSV header
        for line in in_file:
            parts = line.strip().split(',')
            year = int(parts[1])
            price = float(parts[2])
            guitar = Guitar(parts[0], year, price)
            guitars.append(guitar)
    return guitars


def sort_guitars(guitars: list) -> list:
    """Sort list of guitars by oldest to newest."""
    guitars.sort()
    return guitars


def display_guitars(guitars: list):
    """Display all guitars stored in a list."""
    for guitar in guitars:
        print(guitar)


main()
