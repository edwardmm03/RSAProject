from time import process_time
from sympy import nextprime
import random

bit_lengths = [7, 10, 12, 50, 100, 200, 500, 1000, 2400, 10000]

for bit_length in bit_lengths:
    start_time = process_time()
    p = nextprime(random.getrandbits(bit_length))
    q = nextprime(random.getrandbits(bit_length))

    n = p * q
    end_time = process_time()

    print({
        "bit_length": bit_length,
        "time_taken_seconds": (end_time - start_time),
    })
