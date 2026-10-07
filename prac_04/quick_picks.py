"""
CP1404 Prac04 Quick picks
"""
import random

NUMBER_OF_RANDOM_NUMBERS = 6
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    chosen_numbers = []
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while random_number in chosen_numbers:
            random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        chosen_numbers.append(random_number)
    chosen_numbers.sort()
    for number in chosen_numbers:
        print(f"{number:2}", end=" ")
    print()
