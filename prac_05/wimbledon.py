"""
CP1404 Prac 5: Wimbledon
Estimate: 18 minutes
Actual: 22 minutes
"""
import csv

FILE_NAME = "wimbledon.csv"


def main():
    """Read, process and display Wimbledon data."""
    wimbledon_data = read_data(FILE_NAME)
    champion_to_wins, countries = process_data(wimbledon_data)
    display_output(champion_to_wins, countries)


def read_data(file_name):
    """Read CSV file and return reader object."""
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        wimbledon_data = csv.reader(in_file)
    return wimbledon_data


def process_data(wimbledon_data):
    """Process reader data into a dictionary and a set."""
    champion_to_wins = {}
    countries = set()

    next(wimbledon_data)  # Skip CSV header data

    for datum in wimbledon_data:
        champion = datum[2]
        if champion not in champion_to_wins:
            champion_to_wins[champion] = 1
        else:
            champion_to_wins[champion] += 1

        country = datum[3]
        countries.add(country)
    return champion_to_wins, countries


def display_output(champion_to_wins, countries):
    """Display the Wimbledon data."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print(f"These {len(countries)} countries have won Wimbledon:")
    countries = ", ".join(sorted(countries))
    print(f"{countries}")
