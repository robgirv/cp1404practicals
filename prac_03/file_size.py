"""
CP1404 Prac03 File size
"""


def main():
    """Get file name and display number of line in file."""
    file_name = input("File name: ")
    while file_name != "":
        file_size = determine_file_size(file_name)
        print(f"{file_name} has {file_size} lines.")
        file_name = input("File name: ")


def determine_file_size(file_name):
    """Determine how many lines are in a file."""
    with open(file_name) as in_file:
        number_of_lines = len(in_file.readlines())
    return number_of_lines


main()
