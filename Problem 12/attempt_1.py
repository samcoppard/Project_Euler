""" What is the value of the first triangle number to have over five hundred divisors? """

# Every positive integer can be uniquely expressed as a product of primes
# Combinations of 2 and 3 will give the most divisors for the lowest number, so we only
# need to check multiples of 6
# N.B. Update - I don't think is logically sound. The smallest number with >500 divisors
# will definitely be divisible by 6, but not necessarily the smallest triangle number.
# It very likely will be, and in fact it is, but this was not guaranteed, so I got a
# little bit lucky.

import time

start_time = time.time()

from math import sqrt


# Need an efficient way to count how many factors a given number has
def count_factors(num):
    factors = 6  # We're only going to check multiples of 6 here, so we can include the set of factors {1, num, 2, int(num/2), 3, int(num/3)} from the start

    for i in range(4, int(sqrt(num)) + 1):
        if num % i == 0:
            factors += 2

    return factors


max_factors = 0
n = 1

while max_factors < 500:
    triangle_num = (n / 2) * (n + 1)
    if triangle_num % 12 == 0:
        max_factors = max(max_factors, count_factors(triangle_num))
    n += 1

print(
    f"{int(triangle_num)} is the {n}th triangle number, and the first to have over 500 factors - it's got {max_factors} factors"
)

end_time = time.time()

print(f"This took {(end_time - start_time):.3f}s to run")
