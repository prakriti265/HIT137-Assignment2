# Question 1 - Encryption and Decryption Program
# HIT137 Assignment 2

def encrypt_file(shift1, shift2):
    # Open the original file and read its content
    with open("raw_text.txt", "r") as file:
        text = file.read()

    encrypted_text = ""

    for char in text:
        # Lowercase letters
        if char.islower():
            position = ord(char) - ord('a')

            if char <= 'm':  # a-m
                new_pos = (position + shift1 * shift2) % 26
            else:  # n-z
                new_pos = (position - (shift1 + shift2)) % 26

            encrypted_text += chr(new_pos + ord('a'))

        # Uppercase letters
        elif char.isupper():
            position = ord(char) - ord('A')

            if char <= 'M':  # A-M
                new_pos = (position - shift1) % 26
            else:  # N-Z
                new_pos = (position + (shift2 ** 2)) % 26

            encrypted_text += chr(new_pos + ord('A'))

        # Other characters stay the same
        else:
            encrypted_text += char

    # Write encrypted text to file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)


def decrypt_file(shift1, shift2):
    # Open encrypted file
    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted_text = ""

    for char in text:
        if char.islower():
            position = ord(char) - ord('a')

            if char <= 'm':
                new_pos = (position - shift1 * shift2) % 26
            else:
                new_pos = (position + (shift1 + shift2)) % 26

            decrypted_text += chr(new_pos + ord('a'))

        elif char.isupper():
            position = ord(char) - ord('A')

            if char <= 'M':
                new_pos = (position + shift1) % 26
            else:
                new_pos = (position - (shift2 ** 2)) % 26

            decrypted_text += chr(new_pos + ord('A'))

        else:
            decrypted_text += char

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)


def verify_decryption():
    with open("raw_text.txt", "r") as file:
        original = file.read()

    with open("decrypted_text.txt", "r") as file:
        decrypted = file.read()

    if original == decrypted:
        print("Decryption successful")
    else:
        print("Decryption failed")


# MAIN PROGRAM
shift1 = int(input("Enter shift1 value: "))
shift2 = int(input("Enter shift2 value: "))

encrypt_file(shift1, shift2)
decrypt_file(shift1, shift2)
verify_decryption()
