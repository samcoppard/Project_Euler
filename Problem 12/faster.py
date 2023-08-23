""" What is the value of the first triangle number to have over five hundred divisors? """
import time

start_time = time.time()

from math import sqrt


def count_factors(num):
    """Brute force algorithm to see how many factors a number has
    (2 for each divisor - 1 above sqrt(num) and 1 below sqrt(num))"""
    divisors = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            divisors += 2
    return divisors


n = 1  # We'll look at the nth triangle number
max_factors = 0  # The most factors for a triangle number observed so far

while max_factors < 500:
    n += 1

    # The nth triangle number can be calculated as n * (n+1) / 2
    # A number x can be uniquely expressed as the product of primes (x = p1**a1 * p2**a2 * ... * pj**aj)
    # It will have y factors where y = (1 + a1) * (1 + a2) * (1 + a3) * ... * (1 + aj)
    # n and (n+1) are coprime, so to get the number of factors of n*(n+1), you can just
    # multiply the number of factors of n by the number of factors of (n+1)
    if n % 2 == 0:
        num_factors = count_factors(n / 2) * count_factors(n + 1)
    else:
        num_factors = count_factors((n + 1) / 2) * count_factors(n)

    max_factors = max(max_factors, num_factors)

print(
    f"{int((n/2)*(n+1))} has {max_factors} factors, making it the first triangle number to have at least 500 factors"
)

end_time = time.time()

print(f"This took {(end_time - start_time):.3f}s to run")
