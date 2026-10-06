"""
CP1404 Prac03 File size
"""


def main():
    """Get file name and display number of line in file."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            file_size = determine_file_size(filename)
            print(f"{filename} has {file_size} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def determine_file_size(file_name):
    """Determine how many lines are in a file."""
    with open(file_name) as in_file:
        number_of_lines = len(in_file.readlines())
    return number_of_lines


main()
