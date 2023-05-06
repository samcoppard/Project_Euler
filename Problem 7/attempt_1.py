"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

#This is crude but gives the correct answer (104743) very quickly by using the sieve of Eratosthenes

#Make a list with a True entry for each number up to 13**2 == 169
nums = [True]*170
#Set the first two entries in the list to False, because 0 and 1 are not primes
nums[0] = False
nums[1] = False

primes = [2,3,5,7,11,13]

#Sieve of Eratosthenes
for i in primes:
    for j in range(i**2, (max(primes)**2) + 1, i):
        nums[j] = False

#This is where we'll store our list of all primes up to the number 169
primes_2 = []

for i in range(len(nums)):
    if nums[i]:
        primes_2.append(i)

#Then repeat the whole process for numbers up to max(primes_2)**2 i.e. as far as this approach is valid
nums = [True]*27890
nums[0] = False
nums[1] = False

for i in primes_2:
    for j in range(i**2, (max(primes_2)**2) + 1, i):
        nums[j] = False

primes_3 = []

for i in range(len(nums)):
    if nums[i]:
        primes_3.append(i)


#And do it all again, this time only up to 120000 because that's plenty far enough

nums = [True]*120000
nums[0] = False
nums[1] = False

for i in primes_3:
    for j in range(i**2, 119999, i):
        nums[j] = False

primes_4 = []

for i in range(len(nums)):
    if nums[i]:
        primes_4.append(i)


print(primes_4[10000])