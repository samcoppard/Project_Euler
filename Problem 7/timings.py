#Trial division (slow_code) vs sieve of Eratosthenes (fast_code)

import timeit

slow_code = """
x = 10001 #We're looking for the xth prime number

current_prime = 2 #Start with the first prime number
prime_counter = 1 #We've only got one prime number so far
candidate = 3 #This is the next number to check for primarily

#Check every odd number for primality, updating the current_prime and the prime_counter each time, until the prime_counter hits x i.e. you find the one you're looking for
while prime_counter < x:
    for i in range(3, int(candidate**0.5) + 1, 2): #No point checking beyond the sq.rt. of the candidate number
        if candidate % i == 0:
            break
    else:
        current_prime = candidate
        prime_counter += 1
    candidate += 2

print(current_prime)
"""

fast_code = """
x = 10001

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
        if len(primes) == x:  # At this point, we've found the prime we're looking for
            print(f"The {x}th prime number is {primes[-1]}")
            break
        else:
            # Set all multiples of the most recently found prime to False in nums, as they cannot be prime (and you can do this starting from prime**2 to speed things up)
            for j in range(i**2, upper_bound, i):
                nums[j] = False
"""

slow_code_time = timeit.timeit(slow_code, number=10)/10
fast_code_time = timeit.timeit(fast_code, number=10)/10

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))
