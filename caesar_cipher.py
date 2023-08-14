# Day 8 - project 1
import string

# Basci inputs
encrypt_or_decrypt = input(
    "Type 'encrypt' to encrypt a word, and 'decrypt' to decrypt a word: ").lower()
shift_number = int(input("Type the shift number: "))
message = input(f"Type your message: ")

# Shift number is the same for every 26 multiple
while shift_number > 26:
    shift_number -= 26

# Checking for encrypt/decrypt. For decryption it's enoug to reverse the alphabet and move letter with same shift number
if encrypt_or_decrypt == "encrypt":
    ALPHABET = string.ascii_lowercase
elif encrypt_or_decrypt == "decrypt":
    ALPHABET = string.ascii_lowercase[::-1]
else:
    print("Bad input, try 'encrypt' or 'decrypt'")
    exit()


# Main logic
# If it's exceeds len of alphabet it's enough to count shift_number - 26 from beginning of alphabet
encrypted_message = [None] * len(message)
for index, letter in enumerate(message):
    current_shift_number = shift_number
    if ALPHABET.index(letter) + shift_number >= 26:
        current_shift_number = (ALPHABET.index(letter) + shift_number - 26)
        encrypted_message[index] = ALPHABET[current_shift_number]
    else:
        encrypted_message[index] = ALPHABET[ALPHABET.index(
            letter) + shift_number]
print("".join(encrypted_message))
