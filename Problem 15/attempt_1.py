""" Starting in the top left corner of a 2x2 grid, and only being able to move to the right
and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid? """

# The formula (worked out on paper elsewhere) for the number of routes through a mxn grid
# - which I'm going to write from now on as (m,n) - with m,n both integers >= 2, is:
# 2 + [(1, n-1) + (2, n-1) + ... + (m-1, n-1)] + [(m-1, 1) + (m-1, 2) + ... + (m-1, n-1)]

# Also good to note that (a, b) == (b, a) here.

# This all means that we can find the number of routes through any given grid by simply
# adding the number of routes through a set of smaller grids. We just have to use
# memoization to make it speedy

import time

start_time = time.time()

# Set up a list of 21 lists of 21 integers, where we'll store the number of routes through
# grids of different sizes
routes = [[0] * 21 for _ in range(21)]

# Any (1, n) grid will have n + 1 possible routes
for i in range(1, 21):
    routes[i][1] = i + 1


def calc_routes(m, n) -> int:
    if n > m:
        return calc_routes(n, m)  # Reduce duplication
    elif routes[m][n] != 0:
        return routes[m][n]  # Reuse what we've already calculated
    else:
        number_of_routes = (
            2  # Start with the 2 trivial routes around the outside of the grid
        )
        # Implement the formula commented above
        for i in range(1, m):
            # Add the stored number of routes for each subgrid where available; calculate if not available
            if routes[i][n - 1] != 0:
                number_of_routes += routes[i][n - 1]
            else:
                number_of_routes += calc_routes(i, n - 1)
        for j in range(1, n):
            if routes[m - 1][j] != 0:
                number_of_routes += routes[m - 1][j]
            else:
                number_of_routes += calc_routes(m - 1, j)
        # Assign the result to the list of lists of numbers of possible routes
        routes[m][n] = number_of_routes
        return number_of_routes


calc_routes(20, 20)

end_time = time.time()

print(f"There are {routes[20][20]} possible routes through a 20x20 grid")

print(f"This took {(end_time - start_time):.6f} seconds to run")
