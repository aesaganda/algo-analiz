from mimetypes import guess_extension
import random
import string
from itertools import chain, product


def bruteforce():
    # Generate a random string of 10 characters
    # from the string library
    randomString = ''.join(random.choice(string.digits)
                           for i in range(4)) + ''.join(
                               random.choice(string.ascii_lowercase)
                               for i in range(2))

    suffix = randomString[-2:]
    print(randomString)

    chars = string.digits  # chars to look for
    print(suffix)
    for length in range(1, 5):
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            guess = ''.join(attempt) + ''.join(suffix)
            print(guess)
            if guess == randomString:
                print("Sifre=" + '' + guess)
                break


bruteforce()