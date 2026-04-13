from wonderwords import RandomWord
import random
import hang_graphics

# Variables
lives = None
filled_blanks = 0
guessed_word = RandomWord()
words = guessed_word.word(
    word_min_length=2, word_max_length=10, include_categories=["verb"]
)
print(words)

# print(len(words))  # To check the length of the word
lives = len(words)

Blanks = []  # To create a list of blanks for the word
for i in range(len(words)):
    Blanks.append("_")
print(Blanks)

print(hang_graphics.main)  # To print the hangman graphics
print("Welcome to Hangman!")
print(f"Fill in the blanks:")
for i in Blanks:
    print(i, end=" ")
print("\n")

print(f"You have {lives} lives.")

while lives > 0 and filled_blanks < len(words):
    user_guess = input("Guess a letter: ").lower()
    print(user_guess)  # To check the user's guess

    checker = False  # To check if the user's guess is correct
    for i in range(len(words)):
        if user_guess == words[i]:
            Blanks[i] = user_guess
            checker = True
            filled_blanks += 1

    print(Blanks)  # To check the blanks after the user's guess
    if checker == False:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

if lives == 0:
    print(f"You lost! The word was '{words}'{hang_graphics.Game_over}")
else:
    print(
        f"Congratulations! You guessed the word '{words}' correctly!{hang_graphics.Won}"
    )
