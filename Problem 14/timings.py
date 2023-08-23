import timeit

slow_code = """
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
"""

fast_code = """
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
"""

slow_code_time = timeit.timeit(slow_code, number=10)/10
fast_code_time = timeit.timeit(fast_code, number=10)/10

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))
