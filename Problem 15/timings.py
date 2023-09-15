# The combinatorial solution is unsurprisingly a hell of a lot faster (~2500x)

import timeit

slow_code = """
# Set up a list of 21 lists of 21 integers, where we'll store the number of routes through
# grids of different sizes
routes = [[0] * 21 for _ in range(21)]

# Any (1, n) grid will have n + 1 possible routes
for i in range(1, 21):
    routes[i][1] = i + 1

def calc_routes(m, n) -> int:
    if n > m:
        return calc_routes(n, m) # Reduce duplication
    elif routes[m][n] != 0:
        return routes[m][n] # Reuse what we've already calculated
    else:
        number_of_routes = 2 # Start with the 2 trivial routes around the outside of the grid
        # Implement the formula commented above
        for i in range(1, m):
            # Add the stored number of routes for each subgrid where available; calculate if not available
            if routes[i][n-1] != 0:
                number_of_routes += routes[i][n-1]
            else:
                number_of_routes += calc_routes(i, n-1)
        for j in range(1, n):
            if routes[m-1][j] != 0:
                number_of_routes += routes[m-1][j]
            else:
                number_of_routes += calc_routes(m-1, j)
        # Assign the result to the list of lists of numbers of possible routes
        routes[m][n] = number_of_routes
        return number_of_routes


calc_routes(20, 20)
"""

fast_code = """
def calc_routes(n):
    number_of_routes = 1
    for i in range(1, n+1):
        number_of_routes *= ((n+i)/i)
    return round(number_of_routes)
"""

slow_code_time = timeit.timeit(slow_code, number=10) / 10
fast_code_time = timeit.timeit(fast_code, number=10) / 10

print(f"The slow code ran in {slow_code_time:.10f}s")
print(f"The fast code ran in {fast_code_time:.10f}s")

improvement = slow_code_time / fast_code_time

print(f"This is {improvement:.2f}x faster")
