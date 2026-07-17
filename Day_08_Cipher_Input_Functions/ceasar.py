import ceasar_cipher_encryption
import ceasar_cipher_decryption

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = abs(shift)  # to ensure that the shift is always a positive number


def ceasar(text, shift, direction):
    if direction == "encode":
        return ceasar_cipher_encryption.encrypt(text, shift)
    elif direction == "decode":
        return ceasar_cipher_decryption.decrypt(text, shift)
    else:
        return "Invalid direction. Please choose 'encode' or 'decode'."


result = ceasar(text, shift, direction)
print(f"The {direction}d text is: {result}")
