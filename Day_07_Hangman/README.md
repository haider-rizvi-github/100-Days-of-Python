# Day 7: Hangman

This folder contains a simple Hangman game implemented in Python as part of the 100 Days of Python challenge.

## Files

- `hangman.py` - Main game logic. It selects a random word, displays blanks, accepts letter guesses, tracks lives, and shows win/lose results.
- `hang_graphics.py` - A small helper module that contains ASCII art for the Hangman title.
- `Hangman Logic.png` - Optional image showing the game logic or design (if present).

## How it works

1. The game uses the `wonderwords` library to generate a random verb.
2. The number of lives is set to the length of the selected word.
3. The game displays blank spaces for each letter in the word.
4. The player guesses letters one at a time.
5. Correct guesses fill the blank positions.
6. Incorrect guesses reduce the number of lives.
7. The game ends when all letters are guessed or the player runs out of lives.

## Requirements

- Python 3.x
- `wonderwords`

## Installation

```bash
pip install wonderwords
```

## Run the game

From the `Day_7_Hangman` folder:

```bash
python hangman.py
```

## Notes

- The current implementation prints the chosen word and its length to the console for debugging.
- The game expects single-letter guesses and compares them to each character in the chosen word.
- If you want to improve the game, consider adding:
  - input validation for single alphabetic characters
  - a word category selection menu
  - a better hangman drawing for each wrong guess
  - a replay option after the game ends
