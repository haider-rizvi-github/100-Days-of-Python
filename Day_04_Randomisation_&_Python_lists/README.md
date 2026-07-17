# Day 4 — Randomisation & Python Lists

This folder contains beginner Python exercises focused on random number generation using the `random` module and working with Python lists.

## Files

- `CoinFlip.py`
  - Simulates a coin flip using `random.randint(0, 1)`.
  - Prints "Heads" or "Tails" based on the random result.

- `Graphics.py`
  - A module containing ASCII art graphics for Rock, Paper, Scissors, and a draw scenario.
  - Used by the Rock-Paper-Scissors game to display visual representations.

- `Lists.py`
  - Demonstrates basic list operations: creating lists, modifying elements, appending, extending, inserting, removing, popping, and clearing.
  - Also shows nested lists with examples of fruits and vegetables.

- `Randomisation.py`
  - Introduces the `random` module with examples of generating random integers, floats, and uniform distributions.
  - Prints sample random values.

- `Rock_Paper_scissors.py`
  - A text-based Rock-Paper-Scissors game against the computer.
  - User inputs a choice (0 for Rock, 1 for Paper, 2 for Scissors), computer chooses randomly.
  - Displays the result and ASCII art for the computer's choice.
  - Imports the `Graphics` module for visuals.

- `who_pays_bill.py`
  - A bill splitter tool that collects names of people and randomly selects one to pay the bill.
  - Uses a list to store names and `random.choice()` for selection.
  - Includes ASCII art of a bill.

## How to run

Open a terminal in this folder and run the desired script with Python 3:

```bash
python3 CoinFlip.py
python3 Lists.py
python3 Randomisation.py
python3 Rock_Paper_scissors.py
python3 who_pays_bill.py
```

Note: `Graphics.py` is a module and not meant to be run directly.

## Notes

- Ensure Python 3 is installed and the `random` module is available (it's part of the standard library).
- For the Rock-Paper-Scissors game, enter numbers 0, 1, or 2 as prompted.
- These programs illustrate fundamental concepts in randomness and data structures in Python.