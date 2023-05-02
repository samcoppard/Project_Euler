"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# Clean code with a generalised solution below (turned the second section into a function, and adjusted what gets checked to handle even numbers, and output whether the number itself is a prime).
# Note that this generalised solution is less efficient for the actual given problem than the particular solution in solution.py


def is_prime(num):
  if num == 1:
    return False
  elif num == 2:
    return True
  elif num % 2 == 0:
    return False
  else:
    for i in range(3, int(num**0.5) + 1, 2):
      if num % i == 0:
        return False
    return True


def find_largest_prime_factor(a):
  factor_found = False
  for i in range(2, (a + 2) // 2, 1):
    b = a/i
    if b == int(b):
      if is_prime(b):
        print(f"The largest prime factor of {a} is {int(b)}")
        factor_found = True
        break
  if factor_found == False:
    print(f"{a} is a prime number")


find_largest_prime_factor(600851475143)
