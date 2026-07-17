# Building a Ceasar Cipher Encryption Function

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(original_text, shift_amount):

    encrypted_text = ""

    for i in range(len(original_text)):
        position = alphabet.index(original_text[i])
        new_position = (
            position + shift_amount
        ) % 26  # to ensure that the new position wraps around the alphabet if it exceeds 25
        encrypted_text += alphabet[new_position]
    return encrypted_text
