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

    add_new_guitar(guitars)

    save_guitars_to_csv(guitars, "guitars.csv")


def store_guitars(filename: str) -> list:
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


def add_new_guitar(guitars: list):
    """Get and store details for a new guitar."""
    print("Add a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")


def save_guitars_to_csv(guitars: list, filename: str):
    """Save the current list of guitar objects into the CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}")
    print("Guitars saved")


main()
