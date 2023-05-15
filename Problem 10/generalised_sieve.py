"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# Use the Sieve of Eratosthenes to find all primes below x, and then sum them

def sum_of_primes_below(x):

    nums = [True]*(x+1)

    nums[0] = False
    nums[1] = False

    for i in range(4, x + 1, 2):
        nums[i] = False

    primes_sum = 0

    for i in range(x + 1):
        if nums[i] == True:
            primes_sum += i
            for j in range(i**2, x + 1, 2*i):
                nums[j] = False

    print(primes_sum)

sum_of_primes_below(2000000)