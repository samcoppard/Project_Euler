"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

#Generalising here to find the xth prime number. The limit is set by how big you can make the list nums below
x = 1000000

# Use the sieve of Eratosthenes to find all primes below an upper bound of N*ln(N) * 1.3 (because the density of primes is ~N*ln(N) i.e. the 10001st prime is ~ 10001 * ln(10001) == 92114. Then multiply by 1.3 to be on the safe side - could surely make this more efficient with more maths knowledge

#Calculate upper bound i.e. a number that we're pretty sure our desired prime is less than
from math import log
upper_bound = int(x * log(x) * 1.3)

# Make a list with a True entry for each number up to the upper bound
nums = [True]*upper_bound

# Set the first two entries in the list to False, because 0 and 1 are not primes
nums[0] = False
nums[1] = False

# Create a new list to store all the primes, starting with the first prime
primes = [2]

# Check each odd number (no point checking the evens for primality!) to see if it's still True in nums. If it is, it's a prime
for i in range(3, upper_bound, 2):
    if nums[i]:
        primes.append(i)
        if len(primes) == x:  # No point finding more primes after the one we're looking for
            print(f"The {x}th prime number is {primes[-1]}")
            break
        else:
            # Set all multiples of the most recently found prime to False in nums, as they cannot be prime (and you can do this starting from prime**2 to speed things up)
            for j in range(i**2, upper_bound, i):
                nums[j] = False
