"""This is just to play around with how fast the optimised O(1) solution is compared to my original O(n) solution for the sum of squares"""

import timeit

slow_code = """
def sum_of_squares(n):
    return sum([i**2 for i in range(1, n)])
print(sum_of_squares(100000))
"""

fast_code = """
def sum_of_squares(n):
    return (n * (n+1) * ((2*n)+1)) / 6
print(sum_of_squares(100000))
"""

slow_code_time = timeit.timeit(slow_code, number=100)/100
fast_code_time = timeit.timeit(fast_code, number=100)/100

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))