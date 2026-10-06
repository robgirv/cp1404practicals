"""
CP1404 Prac03 Files
"""

# 1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt")
print(f"Hi {in_file.read().strip()}!")
in_file.close()

# 3.
with open("numbers.txt") as in_file:
    numbers = []
    for i in range(2):
        line = int(in_file.readline().strip())
        numbers.append(line)
    print(sum(numbers))

# 4.
with open("numbers.txt") as in_file:
    numbers = []
    for line in in_file:
        numbers.append(int(line.strip()))
    print(sum(numbers))
