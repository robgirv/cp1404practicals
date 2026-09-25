print('''1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program''')
choice = int(input(">>> "))
while choice != 4:
    if choice == 1:
        first_number = int(input("Enter the first number: "))
        last_number = int(input("Enter the last number: "))
        for i in range(first_number, last_number + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == 2:
        first_number = int(input("Enter the first number: "))
        last_number = int(input("Enter the last number: "))
        for i in range(first_number, last_number + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == 3:
        first_number = int(input("Enter the first number: "))
        last_number = int(input("Enter the last number: "))
        for i in range(first_number, last_number + 1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid input")
    print('''1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program''')
    choice = int(input(">>> "))
