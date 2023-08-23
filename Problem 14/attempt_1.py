"""The following iterative sequence is defined for the set of positive integers:

 n --> n/2 (if n is even)
 n --> 3n + 1 (if n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence contains 10 terms.

Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.


Which starting number, under one million, produces the longest chain?

N.B. Once the chain starts the terms are allowed to go above one million."""

import time

start_time = time.time()

dict_nums = {}


def add_empty_value(integer):
    dict_nums[integer] = None


for i in range(1, 1000001):
    add_empty_value(i)


def collatz(starter_num, num=None, counter=1):
    # Set the 2nd argument equal to the 1st argument for convenience
    if num is None:
        num = starter_num
    
    # Find the next number in the Collatz sequence
    if num % 2 == 0:
        next_num = num / 2
    else:
        next_num = 3 * num + 1

    # Return the length of the sequence when it terminates
    if next_num == 1:
        dict_nums[starter_num] = counter + 1
        return counter + 1
    # Or carry out the next step of the sequence if it hasn't yet terminated
    else:
        if next_num in dict_nums and dict_nums[next_num] != None:
            dict_nums[starter_num] = counter + dict_nums[next_num]
            return counter + dict_nums[next_num]
        else:
            counter += 1
            return collatz(starter_num, next_num, counter)


for i in range(1, 1000001):
    collatz(i)

max_key = max(dict_nums, key=dict_nums.get)
max_value = dict_nums[max_key]

#most_steps = max(dict_nums.values())

print(f"The starting number {max_key} produces {max_value} steps, more than any other")

end_time = time.time()
print(f"This code took {(end_time - start_time):.6f}s to run")
