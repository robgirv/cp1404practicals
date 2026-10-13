"""
CP1404 Prac 5: Wimbledon
Estimate: 18 minutes
Actual: ?(9 cont.) minutes
"""
import csv

FILE_NAME = "wimbledon.csv"

champion_to_wins = {}

with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    next(reader)
    for data in reader:
        # print(data)
        champion = data[2]
        print(champion)
