""" What is the value of the first triangle number to have over five hundred divisors? """

# Every positive integer can be uniquely expressed as a product of primes
# Combinations of 2 and 3 will give the most divisors for the lowest number, so we only
# need to check multiples of 6

import time
start_time = time.time()

from math import sqrt

# Need an efficient way to count how many factors a given number has
def count_factors(num):
    factors = {1, num, 2, int(num/2), 3, int(num/3)} # We're only going to check multiples of 6 here

    for i in range(4, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.update([i, int(num/i)])
    
    return(len(factors))


max_factors = 0
n = 1

while max_factors < 500:
    triangle_num = (n/2) * (n+1)
    if triangle_num % 12 == 0:
        max_factors = max(max_factors, count_factors(triangle_num))
    n += 1

print(f"{int(triangle_num)} is the {n}th triangle number, and the first to have over 500 factors - it's got {max_factors} factors")

end_time = time.time()

print(f"This took {(end_time - start_time):.3f}s to run")