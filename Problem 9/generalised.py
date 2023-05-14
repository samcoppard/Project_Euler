"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#Generalised solution for a + b + c = x (although note that if there are multiple valid Pythagorean triples, this algorithm will find the one with the lowest value of a)

#The only faster solution I've seen doesn't work for all values of x e.g. it doesn't work for 3**2 + 4**2 = 5**2

# Rearranging a + b + c = x gives c = x - a - b
# Inserting that into a**2 + b**2 = c**2, then do a bit of algebra on paper, and we get this formula:
# b = (x**2 - (2*x*a)) / (2*x - (2*a))

#Now we just have to check all the possible values of a, noting that we won't have to go beyond a = x/3 as a < b < c (although the loop shouldn't get that far anyway so it doesn't really matter)
def pythag_triplets(x):
    #Store x**2 and 2*x as variables so we don't have to calculate them in every iteration of the for loop
    x_sq = x**2
    x_double = 2*x
    for a in range(1, int(x / 3)):
        b = (x_sq - (x_double*a)) / (x_double - (2*a))
        if int(b) == b: #No point calculating c if b isn't an integer
            c = x - a - b
            print(f"a = {a}, b = {int(b)}, c = {int(c)}, so abc = {int(a*b*c)}")
            break
    else:
        print(f"There is no Pythagorean triplet for which a + b + c = {x}")

pythag_triplets(8192000)