"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

#My solution is in solution.py, a generalised solution is in generalised_solution.py, and the much faster optimised solution (that works in a completely different way) is in optimised.py

import timeit

my_code = """
#Create a function to check if a number is a prime
def is_prime(num):
  #If the number is even, it's obviously not prime (unless it is the number 2 itself, which is trivially prime, so for efficiency's sake we're not including a check for that in this function)
  if num % 2 == 0:
    return False
  else:
    #Check if the number is divisible by any odd number, starting with 3. Note we only need to check possible factors up to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
      #If the number is divisible by any number, then it's not prime
      if num % i == 0:
        return False
    #If we get to this point of the function, then we've checked all possible factors and found none, so the number is prime
    return True


a = 600851475143

#Step through all odd numbers between 3 and our number (a) divided by 3
for i in range(3, (a + 3) // 3, 2):
  #Divide a by each odd number, starting with the smallest. Then check if the result is an integer. If it is, then it's a factor of a. In this way we can generate the largest factors of a
  b = a/i
  if b == int(b):
    #Now we need to check if this factor is prime. The first one that is prime will be our answer
    if is_prime(b):
      print(f"The largest prime factor of {a} is {int(b)}")
      break
"""

optimised_code = """
def primes_up_to_sqrt(n):
  sieve = [True] * (int(n**0.5) + 1)
  sieve[0] = False
  sieve[1] = False
  for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
      for j in range(i**2, int(n**0.5) + 1, i):
        sieve[j] = False

  return [i for i in range(2, (int(n**0.5) + 1)) if sieve[i]]

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
"""

my_time = timeit.timeit(my_code, number = 10)/10
print("My code took {:.6f}s".format(my_time))

optimised_time = timeit.timeit(optimised_code, number = 10)/10
print("The optimised code took {:.6f}s".format(optimised_time))

improvement = my_time / optimised_time

print("The optimised code was {:.2f}x faster than my code".format(improvement))