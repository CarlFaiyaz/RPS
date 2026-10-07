import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Ask the player for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    number_guessing_game()
