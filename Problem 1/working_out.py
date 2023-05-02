# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Sum all the elements of a list containing only the multiples of 3 or 5
mult_sum_10 = sum([i for i in range(1, 10) if i %
                  3 == 0 or i % 5 == 0])  # This is the test case
print(f"Just checking: the test case comes out as {mult_sum_10}")

mult_sum_1000 = sum([i for i in range(1, 1000) if i %
                    3 == 0 or i % 5 == 0])  # This is the solution
print(f"The answer to the problem is {mult_sum_1000}")

# Now for a generalised version


def mult_sum(num):
  return sum([i for i in range(1, num) if i % 3 == 0 or i % 5 == 0])


print(
    f"For multiples of 3 and 5 under 1000000, the answer is {mult_sum(1000000)}")

# The version above has O(n) time complexity

# We can instead create a solution with O(1) time complexity, by summing the multiples of 3 and the multiples of 5 separately, and then subtracting the sum of the multiples of 15. All using the formula for the sum of a arithmetic series


def arith_sum(a, n, d):  # a is first term, #n is number of terms, d is the difference between terms
  return (n/2)*(2*a + (n-1)*d)

# If we set x to be the top of the range, then n = int((x-1)/d). And in the cases we're looking at, a = d


def sum_of_multiples_of_d_below_x(x, d):
  n = int((x-1)/d)
  # Turning this into an integer rather than a float for neatness
  return int((n/2)*(2*d + (n-1)*d))

# In our particular case, we want to find the sum of the multiples of 3 and 5


def sum_of_mults_of_3_and_5_below_x(x):
  return sum_of_multiples_of_d_below_x(x, 3) + sum_of_multiples_of_d_below_x(x, 5) - sum_of_multiples_of_d_below_x(x, 15)


print(sum_of_mults_of_3_and_5_below_x(1000000))

# Turns out integer division is a thing, so n = int((x-1)/d) can instead be just (x-1) // d


def new_sum_of_mults_d_below_x(x, d):
  n = (x-1) // d
  return int((n * (d*(1 + n)) / 2))


def new_sum_of_mults_of_3_and_5_below_x(x):
  return new_sum_of_mults_d_below_x(x, 3) + new_sum_of_mults_d_below_x(x, 5) - new_sum_of_mults_d_below_x(x, 15)


print(new_sum_of_mults_of_3_and_5_below_x(1000000))
