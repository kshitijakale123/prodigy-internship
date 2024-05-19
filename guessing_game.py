import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Continue looping until the user guesses correctly
    while not guessed_correctly:
        try:
            # Prompt the user to input their guess
            guess = int(input("Enter your guess: "))
            number_of_attempts += 1

            # Provide feedback to the user
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {number_of_attempts} attempts.")
        except ValueError:
            # Handle the case where the user input is not an integer
            print("Invalid input. Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    guessing_game()
