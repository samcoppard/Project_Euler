"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# Create a function to check if a number is a prime


def is_prime(num):
  # If the number is even, it's obviously not prime (unless it is the number 2 itself, which is trivially prime, so for efficiency's sake we're not including a check for that in this function)
  if num % 2 == 0:
    return False
  else:
    # Check if the number is divisible by any odd number, starting with 3. Note we only need to check possible factors up to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
      # If the number is divisible by any number, then it's not prime
      if num % i == 0:
        return False
    # If we get to this point of the function, then we've checked all possible factors and found none, so the number is prime
    return True


a = 600851475143

# Step through all odd numbers between 3 and our number (a) divided by 3
for i in range(3, (a + 3) // 3, 2):
  # Divide a by each odd number, starting with the smallest. Then check if the result is an integer. If it is, then it's a factor of a. In this way we can generate the largest factors of a
  b = a/i
  if b == int(b):
    # Now we need to check if this factor is prime. The first one that is prime will be our answer
    if is_prime(b):
      print(f"The largest prime factor of {a} is {int(b)}")
      break
