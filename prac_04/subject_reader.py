"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_data(FILENAME)
    print_subject_details(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like:subject ,lecturer,number of students."""
    with open(filename) as in_file:
        subject_data = []
        for line in in_file:
            line = line.strip().split(',')
            line[2] = int(line[2])
            subject_data.append(line)
    return subject_data


def print_subject_details(subjects):
    """Print the subject details."""
    for i in range(len(subjects)):
        print(f"{subjects[i][0]} is taught by {subjects[i][1]:12} and has {subjects[i][2]:3} students")


main()
