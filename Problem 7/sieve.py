"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

# Use the sieve of Eratosthenes to find all primes below 120000 (because the density of primes is ~N*ln(N) i.e. the 10001st prime is ~ 10001 * ln(10001) == 92114. But 10001 is quite small still, so pinch of salt round up to 120000, so we can be fairly sure we'll go high enough)

# Make a list with a True entry for each number up to 120000
nums = [True]*120000

# Set the first two entries in the list to False, because 0 and 1 are not primes
nums[0] = False
nums[1] = False

#Create a new list to store all the primes, starting with the first prime
primes = [2]

#Check each odd number (no point checking the evens for primality!) to see if it's still True in nums. If it is, it's a prime
for i in range(3, 120000, 2):
    if nums[i]:
        primes.append(i)
        if len(primes) == 10001: #No point finding more primes after the one we're looking for
            print(f"The 10001st prime number is {primes[10000]}")
            break
        else:
            #Set all multiples of the most recently found prime to False in nums, as they cannot be prime (and you can do this starting from prime**2 to speed things up)
            for j in range(i**2, 120000, i):
                nums[j] = False
