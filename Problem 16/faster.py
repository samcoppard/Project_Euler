""" 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? """

# This solution is ~25% faster as it sums over a list comprehension, and both of those
# operations are optimised, whereas my original solution had more python-level operations

import time

start_time = time.time()

sum_of_digits = sum([int(x) for x in str(2**1000)])

end_time = time.time()

print(sum_of_digits)

print(f"This code took {(end_time - start_time):.6f}s to run")