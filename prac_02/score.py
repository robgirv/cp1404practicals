"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Display result based on score alongside a random one."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")

    score = random.randint(0, 100)
    result = determine_result(score)
    print(f"Random: {score} = {result}")


def determine_result(score: float | int) -> str:
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
