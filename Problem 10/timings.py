import timeit

slow_code = """
def sum_of_primes_below(x):

    # Create a list with 2000001 elements. We'll set them all as True to begin with, then change them to False when we know they're not prime
    nums = [True]*(x+1)

    # 0 and 1 are not prime
    nums[0] = False
    nums[1] = False

    # Even numbers are never prime (except for 2, obviously)
    for i in range(4, x + 1, 2):
        nums[i] = False

    # Create a variable to store the running total of the primes found
    primes_sum = 0

    for i in range(x + 1):
        if nums[i] == True:
            primes_sum += i
            for j in range(i**2, x + 1, 2*i):
                nums[j] = False

    print(primes_sum)

sum_of_primes_below(2000000)
"""

fast_code = """
def sum_of_primes_below(x):

    # Create a list with 2000001 elements. We'll set them all as True to begin with, then change them to False when we know they're not prime
    nums = [True]*(x+1)

    # 0 and 1 are not prime
    nums[0] = False
    nums[1] = False

    # Even numbers are never prime (except for 2, obviously)
    for i in range(4, x + 1, 2):
        nums[i] = False

    # Create a variable to store the running total of the primes found
    primes_sum = 0

    # For every number up to sqrt(x), check if its entry in the nums list is True.
    # If it is, it's prime, and we add it to the running total. Then we set the entry for each multiple of this number to be False (note that we can do this in increments of double the number, as all the even multiples are already set to False)
    # If it's False, it's not prime
    for i in range(int((x+1)**0.5) + 1):
        if nums[i] == True:
            primes_sum += i
            for j in range(i**2, x + 1, 2*i):
                nums[j] = False

    # Check if the last value of i in the loop above is even or odd, so we can start the next loop with an odd number, and then only check odd numbers for primality
    if int((x+1)**0.5) % 2 == 0:
        second_loop_start_value = int((x+1)**0.5) + 1
    else:
        second_loop_start_value = int((x+1)**0.5)

    # All we have to do now is check the remaining numbers, and add them to the total if they're prime
    # The trick here is that we don't need to loop over multiples of these numbers, because their multiples will already have been set to False by the previous loop
    # (This same optimisation would make the code from Problem 7 run faster as well)
    for i in range(second_loop_start_value, x+1, 2):
        if nums[i] == True:
            primes_sum += i

    print(primes_sum)

sum_of_primes_below(2000000)
"""

slow_code_time = timeit.timeit(slow_code, number=10)/10
fast_code_time = timeit.timeit(fast_code, number=10)/10

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))
