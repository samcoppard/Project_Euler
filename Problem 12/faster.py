""" What is the value of the first triangle number to have over five hundred divisors? """
import time

start_time = time.time()

from math import sqrt


def count_factors(num):
    divisors = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors += 2
    return divisors


n = 5368
max_factors = 0

while max_factors < 500:
    n += 1

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
