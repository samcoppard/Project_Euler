# Trial division (slow_code) vs sieve of Eratosthenes (fast_code)

import timeit

slow_code = """
for i in range(1,500):
    for j in range(2,500):
        if i<j:
            for k in range(3,500):
                if (j<k):
                    if (i**2) + (j**2) == k**2:
                         if i + j + k == 1000:
                                print (i,j,k)
                                print (i*j*k)
"""

fast_code = """
for a in range(1, 333):
    b = (1000000 - (2000*a)) / (2000 - (2*a))
    if int(b) == b: #No point calculating c if b isn't an integer
        c = 1000 - a - b
        print(f"a = {a}, b = {int(b)}, c = {int(c)}, so abc = {int(a*b*c)}")
"""

slow_code_time = timeit.timeit(slow_code, number=10)/10
fast_code_time = timeit.timeit(fast_code, number=10)/10

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))
