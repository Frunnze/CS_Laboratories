"""
Implements Playfair algorithm
1. prepare the text for encryption
    - uppercase
    - "J" -> "I"
    - couples
    - no spaces and punctuations
    - add "Q", "X", or "Z" between letters of couples with the same letter
2. Construct the encryption matrix.
    - no dublicates in the key (and js)
    - create the matrix by adding to it the key and the alphabet without dublication;
3. Encrypt the message.
    - different rows and columns -> letter is substituted by the letter in the
        same row, but from the column of the other letter;
    - same rows -> letters are substituted by the next letter in the row
    - same columns -> letters are substituted by the next letter in the column;
    - for decryption 1 remains the same, 2 and 3 in the opposite direction;
"""

import re
import random


def is_romanian_language(string):
    """Checks if the letters in the message are romanian letters."""

    pattern = r'^[a-zA-ZăĂâÂșȘțȚîÎ]+$'
    return bool(re.match(pattern, string))


def add_letters(message):
    """Add "Q", "X", or "Z" between letters of couples with the same letter."""

    to_insert = ['Q', 'X', 'Z']
    message, i = list(message), 0

    while i < len(message) - 1:
        if message[i] == message[i+1]:
            message.insert(i+1, random.choice(to_insert))
        i += 2

    # Add an additional letter to the end, in case of an odd message.
    if len(message) % 2 != 0:
        message.append('V')

    return message


def find_letter_indices(letter, matrix):
    """Finds the row and column of a letter."""

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == letter:
                return i, j


def encrypt(message, matrix):
    """Encryption using the Playfair algorithm."""
    
    for i in range(0, len(message), 2):
        letter1, letter2 = message[i], message[i+1]
        row1, column1 = find_letter_indices(letter1, matrix)
        row2, column2 = find_letter_indices(letter2, matrix)
        
        # Implement first condition.
        if row1 != row2 and column1 != column2:
            message[i] = matrix[row1][column2]
            message[i+1] = matrix[row2][column1]

        # Implement second condition.
        elif row1 == row2:
            columns = len(matrix[0])
            next_column1 = (column1 + 1) % columns
            next_column2 = (column2 + 1) % columns
            message[i] = matrix[row1][next_column1]
            message[i+1] = matrix[row2][next_column2]

        # Implement third condition.
        elif column1 == column2:
            rows = len(matrix)
            next_row1 = (row1 + 1) % rows
            next_row2 = (row2 + 1) % rows
            message[i] = matrix[next_row1][column1]
            message[i+1] = matrix[next_row2][column2]

    return "".join(message)


def decrypt(ciphertext, matrix):
    """Decryption using the Playfair algorithm."""
    
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i+1]
        row1, column1 = find_letter_indices(letter1, matrix)
        row2, column2 = find_letter_indices(letter2, matrix)
        
        # Implement first condition.
        if row1 != row2 and column1 != column2:
            ciphertext[i] = matrix[row1][column2]
            ciphertext[i+1] = matrix[row2][column1]

        # Implement second condition.
        elif row1 == row2:
            columns = len(matrix[0])
            next_column1 = (column1 - 1) % columns
            next_column2 = (column2 - 1) % columns
            ciphertext[i] = matrix[row1][next_column1]
            ciphertext[i+1] = matrix[row2][next_column2]

        # Implement third condition.
        elif column1 == column2:
            rows = len(matrix)
            next_row1 = (row1 - 1) % rows
            next_row2 = (row2 - 1) % rows
            ciphertext[i] = matrix[next_row1][column1]
            ciphertext[i+1] = matrix[next_row2][column2]
    
    # Eliminate the added Q, X, or Z
    i = 0
    while i < len(ciphertext) - 2:
        if (ciphertext[i] == ciphertext[i+2] and 
            ciphertext[i+1] in ['Q', 'X', 'Z']):
            del ciphertext[i+1]
            i += 1
        else:
            i += 2

    # Eliminate the last letter added by you.
    if ciphertext[-1] == "V":
        ciphertext.pop()

    return "".join(ciphertext)


def create_matrix(key):
    """Make the matrix with 5 rows and 6 columns."""

    matrix = []
    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    new_alphabet = ''.join(dict.fromkeys(key + alphabet))

    for i in range(0, 30, 6):
        row = new_alphabet[i:i+6]
        matrix.append(list(row))

    return matrix


def input_key():
    """Input a valid key."""

    key = input("\tKey: ")
    key = key.replace(" ", "")
    while not (is_romanian_language(key) and len(key) >= 7):
        print("\tChars have to be in the interval 'A'-'Z', 'a'-'z'" \
            ", and the key has to be equal or greater than 7.")
        key = input("\tKey: ")
        key = key.replace(" ", "")

    key = key.upper()
    key = key.replace("J", "I")
    key = ''.join(dict.fromkeys(key)) # Eliminate dublicates.

    return key


if __name__ == "__main__":
    # Implements the menu.
    print('Menu:')
    print('\taction: e - encryption; d - decryption; x - exit;')
    print('\tmessage: a string of Romanian letters (optionally with spaces).')
    print('\tkey: a string of Romanian letters with a length of 7 or greater.')

    while True:
        command = input("\nAction: ")
        if command == "e":
            # Add the message and check if it is valid.
            message = input("\tMessage: ")
            message = message.replace(" ", "")
            while not is_romanian_language(message):
                print("\tChars have to be in the interval 'A'-'Z', 'a'-'z'" \
                    " of the Romanian language.")
                message = input("\tMessage: ")
                message = message.replace(" ", "")

            # Process the text to uppercase and "J" -> "I".
            message = message.upper()
            message = message.replace("J", "I")

            # Add "Q", "X", or "Z".
            message = add_letters(message)

            # Get the key.
            key = input_key()
            
            # Make the matrix.
            matrix = create_matrix(key)

            # Encrypt the message.
            ciphertext = encrypt(message, matrix)
            print("\tCiphertext: " + ciphertext) 

        elif command == "d":
            # Add the ciphertext.
            ciphertext = input("\tCiphertext: ")
            ciphertext = ciphertext.upper()
            while not (is_romanian_language(ciphertext) and "J" not in ciphertext):
                print("\tChars have to be in the interval 'A'-'Z', 'a'-'z'" \
                    " without 'J' or 'j'")
                ciphertext = input("\tCiphertext: ")
                ciphertext = ciphertext.upper()

            # Process the ciphertext.
            ciphertext = ciphertext.replace(" ", "")
            ciphertext = list(ciphertext)

            # Get the key.
            key = input_key()

            # Make the matrix.
            matrix = create_matrix(key) 

            # Decrypt the ciphertext.
            decrypted_message = decrypt(ciphertext, matrix)
            print("\tMessage: " + decrypted_message)

        elif command == "x":
            break