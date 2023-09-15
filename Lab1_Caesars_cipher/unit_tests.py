import unittest
from main import encrypt, decrypt


class TestAddition(unittest.TestCase):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test1_encrypt_with_key1(self):
        message = 'CIFRULCEZAR'
        key1 = 3
        result = encrypt(self.alphabet, message, key1)
        answer = 'FLIUXOFHCDU'
        self.assertEqual(result, answer)

    def test2_encrypt_with_key1(self):
        message = 'BRUTEFORCEATTACK'
        key1 = 17
        result = encrypt(self.alphabet, message, key1)
        answer = 'SILKVWFITVRKKRTB'
        self.assertEqual(result, answer)

    def test3_encrypt_with_both_keys(self):
        message = 'BRUTEFORCEATTACK'
        key1, key2 = 3, 'CRYPTOGRAPHY'
        result = encrypt(self.alphabet, message, key1, key2)
        answer = 'FTXAJKHTPJDAADPN'
        self.assertEqual(result, answer)

    def test1_decrypt_with_key1(self):
        encrypted_message = 'FLIUXOFHCDU'
        key1 = 3
        result = decrypt(self.alphabet, encrypted_message, key1)
        answer = 'CIFRULCEZAR'
        self.assertEqual(result, answer)

    def test2_decrypt_with_key1(self):
        encrypted_message = 'SILKVWFITVRKKRTB'
        key1 = 17
        result = decrypt(self.alphabet, encrypted_message, key1)
        answer = 'BRUTEFORCEATTACK'
        self.assertEqual(result, answer)

    def test3_decrypt_with_both_keys(self):
        encrypted_message = 'FTXAJKHTPJDAADPN'
        key1, key2 = 3, 'CRYPTOGRAPHY'
        result = decrypt(self.alphabet, encrypted_message, key1, key2)
        answer = 'BRUTEFORCEATTACK'
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()