import itertools
from os import read
import string
import time

def guess_common_passwords(password):
    with open('common_passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()
    
    for i, match in enumerate(data):
        if match == password:
            return f'The password is {match} (Common password number #{i})'

    return 0

def brute_force(password, min_length=4,max_length=9):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for password_length in range(min_length,max_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f'The password is {guess} (Attempts #{attempts})'
            print(guess, attempts)

def get_password(password):
    common = guess_common_passwords(password)
    return brute_force(password) if common == 0 else common

start_time = time.time()

# print(get_password('abcd123'))
# print(round(time.time() - start_time, 2), "sec")

user_password = input("Enter you password to check its efficiency: ")
print(get_password(user_password))
print(round(time.time() - start_time, 2), "sec")
  