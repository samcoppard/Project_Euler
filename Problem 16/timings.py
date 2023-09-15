import timeit

slow_code = """
x = str(2**1000)

sum_of_digits = 0
for i in range(len(x)):
    sum_of_digits += int(x[i])
"""

fast_code = """
sum([int(x) for x in str(2**1000)])
"""

slow_code_time = timeit.timeit(slow_code, number=100) / 100
fast_code_time = timeit.timeit(fast_code, number=100) / 100

print(f"The slow code ran in {slow_code_time:.6f}s")
print(f"The fast code ran in {fast_code_time:.6f}s")

print(f"This is a {(slow_code_time / fast_code_time):.2f}x improvement")