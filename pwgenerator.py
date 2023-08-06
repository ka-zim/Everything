# Simple password generator:  

import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"
password = ''
size = int(input('Password character length: '))

for _ in range(size):
    x = random.randint(0, len(characters) - 1)
    password += characters[x]

print(password)