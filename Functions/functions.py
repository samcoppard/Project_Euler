from math import sqrt

def generate_primes(num) -> list:
    """Generate a list of all primes <= num using the sieve of Eratosthenes.
    Logic explained in generalised_sieve.py from Problem 10"""
    if num == 0 or num == 1:
        return None
    elif num == 2:
        return [2]

    primes = []

    nums = [True] * (num + 1)
    nums[0] = False
    nums[1] = False

    for i in range(4, num + 1, 2):
        nums[i] = False

    for i in range(int(sqrt(num + 1)) + 1):
        if nums[i] == True:
            primes.append(i)
            for j in range(i**2, num + 1, 2 * i):
                nums[j] = False

    if int((num + 1) ** 0.5) % 2 == 0:
        second_loop_start_value = int((num + 1) ** 0.5) + 1
    else:
        second_loop_start_value = (
            int((num + 1) ** 0.5) + 2
        )  # Added the +2 at the end so we don't get the same prime in the list of primes twice

    for i in range(second_loop_start_value, num + 1, 2):
        if nums[i] == True:
            primes.append(i)

    return primes


def prime_factorise(num, list_of_factors) -> list:
    for prime in generate_primes(int(num)):
        if num % prime == 0:
            list_of_factors.append(prime)

            if num / prime == 1:
                return list_of_factors
            else:
                return prime_factorise(num / prime, list_of_factors)