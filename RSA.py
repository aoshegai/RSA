import random
from sympy import primerange

primes = list(primerange(1, 10*6))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

class RSA:
    def __init__(self):
        self.p = random.choice(primes)
        self.q = random.choice(primes)
        while self.q == self.p:
            self.q = random.choice(primes)

        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        self.e = random.randrange(1, self.phi_n)
        while gcd(self.e, self.phi_n) != 1:
            self.e = random.randrange(1, self.phi_n)
        
        self.d = modinv(self.e, self.phi_n)

    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)
