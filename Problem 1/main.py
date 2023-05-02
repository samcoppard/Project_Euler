# Went into an optimised general case here - see working_out.py to see how I ended up here

# The O(n) solution
import timeit


def slow_mult_sum(num):
  return sum([i for i in range(1, num) if i % 3 == 0 or i % 5 == 0])

# The O(1) solution


def fast_sum_of_mults_of_d_below_x(x, d):
  n = (x-1) // d
  return int((n * (d*(1 + n)) / 2))


def fast_mult_sum(num):
  return fast_sum_of_mults_of_d_below_x(num, 3) + fast_sum_of_mults_of_d_below_x(num, 5) - fast_sum_of_mults_of_d_below_x(num, 15)


# Time to test how fast each one works by summing the multiples of 3 and 5 below 10 million (10000000)


slow_code_to_test = """
def slow_mult_sum(num):
  return sum([i for i in range(1,num) if i % 3 == 0 or i % 5 == 0])
slow_mult_sum(10000000)
"""

# Use the timeit library to run the code 10 times, then take an average of the times taken
slow_elapsed_time = timeit.timeit(slow_code_to_test, number=10)/10

# Print how long it took in seconds, to 6 d.p.
print("Time taken for slow code: {:.6f}s".format(slow_elapsed_time))


fast_code_to_test = """
def fast_sum_of_mults_of_d_below_x(x,d):
  return int((((x-1) // d) * (d*(1 + (x-1) // d))) / 2)

def fast_mult_sum(num):
  return fast_sum_of_mults_of_d_below_x(num, 3) + fast_sum_of_mults_of_d_below_x(num, 5) - fast_sum_of_mults_of_d_below_x(num, 15)
fast_mult_sum(10000000)
"""

fast_elapsed_time = timeit.timeit(fast_code_to_test, number=10)/10

print("Time taken for fast code: {:.6f}s".format(fast_elapsed_time))

# Calculate the speed improvement to 2 d.p.
speed_improvement = slow_elapsed_time / fast_elapsed_time

print("The new solution is {:.2f}x faster".format(speed_improvement))

# Using num = 10,000,000, the improved cost is 500k times faster!
