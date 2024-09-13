def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("That's not a valid number. Please try again.")

    if numbers:
        min_number = min(numbers)
        max_number = max(numbers)
        print(f"The smallest number is: {min_number}")
        print(f"The largest number is: {max_number}")
    else:
        print("No numbers were entered.")


# Call the function to run the program
find_min_max()
