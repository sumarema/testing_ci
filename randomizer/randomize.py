import secrets
import random


def _get_secret_number():
    return secrets.choice(list(range(1, 10)))


def _get_random_number():
    return random.randrange(1, 10, 1)


secret_number = _get_secret_number()
rand_number = _get_random_number()

print(secret_number)
print(rand_number)
