def encrypt(alphabet, message, key1, key2=''):
    """Encrypts the given message with Caesar's cipher using the given keys."""

    # Makes a new alphabet order, if we have key2.
    if key2:
        alphabet = ''.join(dict.fromkeys(key2 + alphabet))
        print('   New alphabet: ' + alphabet)

    # Associates letters to the indices of letters used to encrypt the message.
    map = {letter: (index + key1) % 26 for index, letter in enumerate(alphabet)}

    # Encrypts the message.
    encrypted_message = ''
    for letter in message:
        encrypted_message += alphabet[map[letter]]

    return encrypted_message


def decrypt(alphabet, encrypted_message, key1, key2=''):
    """Decrypts the given encrypted message."""

    # Makes a new alphabet order, if we have key2.
    if key2:
        alphabet = ''.join(dict.fromkeys(key2 + alphabet))
        print('   New alphabet: ' + alphabet)

    # Associates letters to the indices of letters used to decrypt the message.
    map = {letter: (index - key1) % 26 for index, letter in enumerate(alphabet)}

    # Decrypts the message.
    decrypted_message = ''
    for letter in encrypted_message:
        decrypted_message += alphabet[map[letter]]

    return decrypted_message


def input_message():
    """Inputs the message and formats it."""

    correct_message = False
    while not correct_message:
        message = input('   Message: ')
        message = message.replace(' ', '')
        message = message.upper()

        if message.isalpha():
            correct_message = True
        else:
            print("   Chars have to be in the range 'A'-'Z' or 'a'-'z'")
    return message


def input_key1():
    """Inputs key1 and satisfies its limits."""

    key1 = input("   key1: ")
    while not (key1.isdigit() and int(key1) >= 1 and int(key1) <= 25):
        print('   key1 has to be an integer between 1 - 25')
        key1 = input("   key1: ")
    return int(key1)


def input_key2():
    """Inputs key2, formats it, and satisfies its limits."""

    correct_key2 = False
    while not correct_key2:
        key2 = input("   key2: ").upper()
        if key2 == '-':
            key2 = ''
            break
        elif key2.isalpha() and len(key2) >= 7:
            correct_key2 = True
        else:
            print('   key2 has to be made only of english letters, '\
                    'with a length of at least 7')
    return key2
    

if __name__ == '__main__':
    # Implements the menu.
    print('Menu:')
    print('\taction: e - encryption; d - decryption; x - exit;')
    print('\tmessage: a string of English letters (optionally with spaces).')
    print('\tkey1: an integer from 1 to 25 including')
    print('\tkey2: a string of English letters, '\
          'with a length of at least 7; add "-" to not use it;')

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:        
        action = input("\nAction: ")
        if action == 'e':
            message = input_message()
            key1 = input_key1()
            key2 = input_key2()
            print("   Encrypted message: ", \
                  encrypt(alphabet, message, key1, key2))
        elif action == 'd':
            encrypted_message = input_message()
            key1 = input_key1()
            key2 = input_key2()
            print("   Decrypted message: ", \
                  decrypt(alphabet, encrypted_message, key1, key2))
        elif action == 'x':
            break
        else: 
            print('Action is not valid.')