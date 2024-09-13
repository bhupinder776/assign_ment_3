def login():
    # Define the correct username and password
    correct_username = "python"
    correct_password = "rules"

    # Number of attempts
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        # Get username and password from the user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the entered credentials are correct
        if username == correct_username and password == correct_password:
            print("Welcome")
            return  # Exit the function when login is successful

        # Increment the attempt counter
        attempts += 1

        # Check if maximum attempts are reached
        if attempts < max_attempts:
            print(f"Incorrect credentials. You have {max_attempts - attempts} attempt(s) left.")
        else:
            print("Access denied")


# Call the function to start the login process
login()
