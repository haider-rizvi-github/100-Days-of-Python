import random
import ascii_art

computer_guess = random.randint(1, 100)
levels = {"Easy": 10, "Hard": 5}

print(ascii_art.main)  # prints the ascii art for the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ").title()


print(f"You have {levels[difficulty]} attempts remaining to guess the number.")

# only use this line for testing purposes, comment it out when you are done testing
# print(f"Pssst, the correct answer is {computer_guess}")

guess = int(input("Make a guess: "))

# Check that the guess is between 1 and 100
while guess < 1 or guess > 100:
    print("Please enter a number between 1 and 100.")
    guess = int(input("Make a guess: "))


# Main guessing loop and it will end once the user guesses the number or runs out of attempts
while guess != computer_guess and levels[difficulty] > 1:

    difference = abs(computer_guess - guess)

    if difference <= 5:
        print("You are close!")

    elif guess < computer_guess:
        print("Too low.")

    elif guess > computer_guess:
        print("Too high.")

    levels[difficulty] -= 1

    print(f"You have {levels[difficulty]} attempts remaining " "to guess the number.")

    guess = int(input("Make a guess: "))

    # Validating every new guess
    while guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        guess = int(input("Make a guess: "))


if guess == computer_guess:
    print(f"You got it! The answer was {computer_guess}.")
else:
    print(f"You've run out of guesses. The answer was {computer_guess}.")
