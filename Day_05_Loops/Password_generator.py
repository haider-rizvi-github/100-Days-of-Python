# Password Generator Project
import random

print("Welcome to the PyPassword Generator!")

Password_length = int(input("How many characters would you like in your password? "))
include_numbers = int(input("How many numbers would you like in your password? "))
include_symbols = int(input("How many symbols would you like in your password? "))

if include_numbers + include_symbols > Password_length:
    print("The number of numbers and symbols cannot exceed the total password length.")
    exit()
else:
    # Storing ASCII values in Lists
    Letters = []
    Numbers = []
    Symbols = []

    for i in range(33, 127):
        if (
            i >= 33
            and i <= 47
            or i >= 58
            and i <= 64
            or i >= 91
            and i <= 96
            or i >= 123
            and i <= 126
        ):
            Symbols.append(chr(i))
        elif i >= 48 and i <= 57:
            Numbers.append(chr(i))
        else:
            Letters.append(chr(i))

    # Generating the password
    Password = []
    for i in range(Password_length):
        if include_numbers >= 1:
            Password.append(random.choice(Numbers))
            include_numbers -= 1
        elif include_symbols >= 1:
            Password.append(random.choice(Symbols))
            include_symbols -= 1
        else:
            Password.append(random.choice(Letters))

    # Printing the password
    print(f"Your Password is: {''.join(Password)} ")
