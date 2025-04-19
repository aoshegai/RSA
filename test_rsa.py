import unittest
import random
from sympy import primerange
from math import gcd
from RSA import RSA

primes = list(primerange(1, 10*6))

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def modinv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return 0
    else:
        return x % m

class TestRSA(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(25, 35), 5)
        self.assertEqual(gcd(7, 13), 1)
        self.assertEqual(gcd(0, 10), 10)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(15, 15), 15)
        self.assertEqual(gcd(1071, 462), 21)

    def test_modinv(self):
        self.assertEqual(modinv(3, 11), 4)
        self.assertEqual(modinv(7, 26), 15)
        self.assertEqual(modinv(1, 5), 1)
        self.assertEqual(modinv(5, 1), 0)
        self.assertEqual(modinv(11, 3), 2)
        self.assertEqual(modinv(17, 3120), 2753)

        self.assertEqual(modinv(4, 6), 0)
        self.assertEqual(modinv(6, 4), 0)
        self.assertEqual(modinv(12, 18), 0)

    def test_modinv_no_inverse(self):
        self.assertEqual(modinv(2, 4), 0)

    def test_encryption_decryption_edge_cases(self):
        rsa = RSA()
        n = rsa.n

        message0 = 0
        ciphertext0 = rsa.encrypt(message0)
        decrypted_message0 = rsa.decrypt(ciphertext0)
        self.assertEqual(decrypted_message0, message0)

        message1 = 1
        ciphertext1 = rsa.encrypt(message1)
        decrypted_message1 = rsa.decrypt(ciphertext1)
        self.assertEqual(decrypted_message1, message1)

        message_near_n = n - 1
        ciphertext_near_n = rsa.encrypt(message_near_n)
        decrypted_message_near_n = rsa.decrypt(ciphertext_near_n)
        self.assertEqual(decrypted_message_near_n, message_near_n)

    def test_rsa_max_message_size(self):
        rsa = RSA()
        message = rsa.n - 1
        ciphertext = rsa.encrypt(message)
        decrypted_message = rsa.decrypt(ciphertext)
        self.assertEqual(decrypted_message, message)

        message_too_big = rsa.n + 1
        ciphertext_too_big = rsa.encrypt(message_too_big)
        decrypted_message_too_big = rsa.decrypt(ciphertext_too_big)
        self.assertNotEqual(decrypted_message_too_big, message_too_big)

    def test_random_messages(self):
        rsa = RSA()

        message_range_max = rsa.n - 1

        num_messages = 10
        random_messages = [random.randint(1, message_range_max) for _ in range(num_messages)]

        for message in random_messages:
            ciphertext = rsa.encrypt(message)
            decrypted_message = rsa.decrypt(ciphertext)
            self.assertEqual(decrypted_message, message, f"Test failed for message: {message}")


if __name__ == '__main__':
    unittest.main()

