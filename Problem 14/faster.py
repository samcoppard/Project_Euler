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

dict = {}

dict[1] = 4
dict[2] = 2


def add_empty_value(integer):
    dict[integer] = None


for i in range(3, 1000001):
    add_empty_value(i)


def collatz(starter_num, num=None, counter=1, incidentals=[]):
    # Find the next number in the Collatz sequence
    if num % 2 == 0:
        next_num = num / 2
    else:
        next_num = 3 * num + 1

    # Return the length of the sequence so far, plus the length of the sequence
    # starting at next_num if that's already been calculated
    if next_num in dict and dict[next_num] != None:
        dict[starter_num] = counter + dict[next_num]
        for ele in incidentals:
            if ele in dict:
                dict[ele] = counter + dict[next_num] - (incidentals.index(ele) + 1)
        return counter + dict[next_num]
    # Or carry out the next step of the sequence if it hasn't yet terminated
    else:
        incidentals.append(next_num)
        counter += 1
        return collatz(starter_num, next_num, counter, incidentals)


for i in range(3, 1000001):
    if dict[i] == None:
        collatz(i, i, 1, [])

max_key = max(dict, key=dict.get)
max_value = dict[max_key]

print(f"The starting number {max_key} produces {max_value} steps, more than any other")


end_time = time.time()
print(f"This code took {(end_time - start_time):.6f}s to run")
