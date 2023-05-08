"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

#Without knowing a rough upper limit, we wouldn't be able to use the sieve of Eratosthenes. So let's have a go at trial division as well.
#Interestingly the approach below is MUCH faster than storing all the primes in a list, even though that approach means you only have to check if a number is divisible by any of those primes to determine primality

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