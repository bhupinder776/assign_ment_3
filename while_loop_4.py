import random


def guess_number_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    while True:
        # Get the user's guess
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Correct!")
            break  # Exit the loop when the user guesses correctly


# Call the function to start the game
guess_number_game()
