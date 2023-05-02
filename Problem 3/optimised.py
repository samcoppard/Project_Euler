#Generate a list of prime numbers up to the square root of n (no point going past this in our case) using the sieve of Eratosthenes
#Explanation here if required - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def primes_up_to_sqrt(n):
  sieve = [True] * (int(n**0.5) + 1)
  sieve[0] = False
  sieve[1] = False
  for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
      for j in range(i**2, int(n**0.5) + 1, i):
        sieve[j] = False

  return [i for i in range(2, (int(n**0.5) + 1)) if sieve[i]]



#Find the largest prime factor of n.
"""We do this by getting a list of all the primes up to the square root of n, and then dividing n by each of the possible prime factors, until we're left with the number 1.

This makes use of the fact that every integer can be expressed as the product of primes, and it can only be done so in one way (the Fundamental Theorem of Arithmetic).

So e.g. 6936 = 2**3 * 3 * 17**2. Using the algorithm below, we'd get:
6936 / 2 = 3468
3468 / 2 = 1734
1734 / 2 = 867
867 / 3 = 289
289 / 17 = 17
17 / 17 = 1
So it spits out 17 as the largest prime factor
"""

def largest_prime_factor(n):
    prime_list = primes_up_to_sqrt(n)
    i = 0
    while i < len(prime_list):
        if n % prime_list[i] == 0:
            n //= prime_list[i]
            if n == 1:
              return prime_list[i]
        else:
            i += 1
    if n > 1:
        return n

n = 600851475143

print(f"The largest prime factor of {n} is {largest_prime_factor(n)}")
