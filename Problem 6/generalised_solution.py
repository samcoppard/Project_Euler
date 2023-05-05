"""The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + ... + 10**2 == 385

The square of the sum of the first ten natural numbers is (1+2+...+10)**2 == 55**2 == 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 == 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

n = 100

# The sum of an arithmetic sequence is (n/2)*(a+L) where n is the number of terms, a is the first number in the sequence, and L is the last number in the sequence
def square_of_sum(n):
    return ((n / 2) * (n + 1)) ** 2

# The formula for the sum of the first n consecutive squares is (n*(n+1)*((2*n)+1))/6.
def sum_of_squares(n):
    return (n * (n+1) * ((2*n)+1)) / 6

print(f"The difference is {int(square_of_sum(n) - sum_of_squares(n))}")
