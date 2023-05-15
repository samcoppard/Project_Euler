"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# Use the Sieve of Eratosthenes to find all primes below two million, and then sum them

# Create a list with 2000001 elements. We'll set them all as True to begin with, then change them to False when we know they're not prime
nums = [True]*2000001

# 0 and 1 are not prime
nums[0] = False
nums[1] = False

# Even numbers are never prime (except for 2, obviously)
for i in range(4, 2000001, 2):
    nums[i] = False

# Create a variable to store the running total of the primes found
primes_sum = 0

# For every number up to sqrt(2000001), check if its entry in the nums list is True.
# If it is, it's prime, and we add it to the running total. Then we set the entry for each multiple of this number to be False (note that we can do this in increments of double the number, as all the even multiples are already set to False)
# If it's False, it's not prime
for i in range(int(2000001**0.5)+1):
    if nums[i] == True:
        primes_sum += i
        for j in range(i**2, 2000001, 2*i):
            nums[j] = False

# Check if the last value of i in the loop above is even or odd, so we can start the next loop with an odd number, and then only check odd numbers for primality
if int(2000001**0.5) % 2 == 0:
    x = int(2000001**0.5) + 1
else:
    x = int(2000001**0.5)

# All we have to do now is check the remaining numbers, and add them to the total if they're prime
# The trick here is that we don't need to loop over multiples of these numbers, because their multiples will already have been set to False by the previous loop
# (This same optimisation would make the code from Problem 7 run faster as well)
for i in range(x, 2000001, 2):
    if nums[i] == True:
        primes_sum += i

print(primes_sum)
