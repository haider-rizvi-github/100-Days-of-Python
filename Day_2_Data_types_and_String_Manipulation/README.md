# 100 Days of Python - Day 2: Data Types and String Manipulation

This folder covers Day 2 of the "100 Days of Python" challenge, focusing on Python data types (strings, integers, floats, booleans), type conversions, string slicing, and basic calculations with user input.

## Files

- `Data_types.py`
  - Demonstrates Python data types and operations.
  - String slicing (e.g., phone number extraction).
  - Differences between string concatenation and numeric addition.
  - Using `len()` for strings.
  - Type checking with `type()`.
  - Type conversions (`int()`, `float()`, `str()`, `bool()`).
  - Interactive example: counts letters in user's name.

- `Tip_calculator.py`
  - Calculates tip and splits bill among people.
  - Inputs: total bill (float), tip percentage (float), number of people (int).
  - Computes tip amount, total with tip, and per-person share.
  - Outputs the amount each person should pay.

- `BMI_calculator.py`
  - Body Mass Index (BMI) calculator.
  - Inputs: weight in kg (float), height in meters (float).
  - Calculates BMI and categorizes weight status:
    - <25: Optimum
    - 25-30: Overweight
    - 30-35: Obese Class I
    - 35-40: Obese Class II
    - >40: Obese Class III

## What I Learned

- Python's main data types: `str`, `int`, `float`, `bool`.
- String indexing and slicing (positive and negative).
- Type conversion functions and their behaviors.
- Mathematical operations vs. string operations.
- Using `input()` for user data and converting types.
- Basic conditional statements (`if-elif-else`) for decision-making.
- F-string formatting for output.
- Order of operations in expressions.

## Run Locally

In the terminal, navigate to this folder and run:

```bash
python3 Data_types.py
python3 Tip_calculator.py
python3 BMI_calculator.py
```

## Notes

- These scripts build on Day 1 basics, introducing data handling and calculations.
- All inputs are validated by type conversion (e.g., `float(input(...))`).
- The BMI calculator includes health categories based on standard ranges.</content>
<parameter name="filePath">/home/syed/Desktop/100 Days of Python/Day_2_Data_types_and_String_Manipulation/README.md