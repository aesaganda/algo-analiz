from itertools import product

chars = '0123456789'  # chars to look for

for length in range(1, 3):  # only do lengths of 1 + 2
    to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
        print(''.join(attempt))