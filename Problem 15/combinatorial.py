""" Starting in the top left corner of a 2x2 grid, and only being able to move to the right
and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid? """

# There's a much faster combinatorial approach. The full details are here:
# https://projecteuler.net/overview=0015

# The gist is that for a mxn grid, the question is equivalent to asking how many ways
# there are to place m movements to the right (out of m+n total movements).
# This is given by (m+n)! / [n! * (m+n-m)!]
# As m == n for a square grid, this simplifies down to (2n)! / (n! ** 2)
# This in turn simplifies to the product of (n+i)/i for i between 1 and n


def calc_routes(n):
    number_of_routes = 1
    for i in range(1, n + 1):
        number_of_routes *= (n + i) / i
    return round(number_of_routes)


print(calc_routes(20))
