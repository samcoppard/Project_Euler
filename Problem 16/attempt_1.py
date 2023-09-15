""" 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? """

import time

start_time = time.time()

x = str(2**1000)

sum_of_digits = 0
for i in range(len(x)):
    sum_of_digits += int(x[i])

end_time = time.time()

print(sum_of_digits)

print(f"This code took {(end_time - start_time):.6f}s to run")