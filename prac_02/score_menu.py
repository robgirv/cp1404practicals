"""Use a score to determine the result or show stars based on score."""


def main():
    """Get score to determine result or show stars."""
    score = 0
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ")
    while choice.upper() != "Q":
        if choice.upper() == "G":
            score = get_valid_score()
        elif choice.upper() == "P":
            result = determine_result(score)
            print(f"User score {score} is {result}")
        elif choice.upper() == "S":
            print("*" * int(score))
        else:
            print("Error: Invalid input")
            print(menu)
            choice = input(">>> ")
        print(menu)
        choice = input(">>> ")
    print("Farewell")


def get_valid_score() -> float:
    """Get a valid score between 0 and 100 inclusive."""
    valid_score = float(input("Enter your score (0 to 100): "))
    while valid_score < 0 or valid_score > 100:
        print("Error: Invalid input")
        valid_score = float(input("Enter your score (0 to 100): "))
    return valid_score


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
