# building a ceasar cipher decryption function

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


def decrypt(original_text, shift_amount):

    decrypted_text = ""

    for i in range(len(original_text)):
        position = alphabet.index(original_text[i])
        new_position = (
            position - shift_amount
        ) % 26  # to ensure that the new position wraps around the alphabet if it goes below 0
        decrypted_text += alphabet[new_position]
    return decrypted_text
