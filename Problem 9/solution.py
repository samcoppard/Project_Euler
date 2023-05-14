"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#This is a fast but very specific solution. Testing shows it's more than 50,000x faster than using the most obviously obvious solution iterating over 1<500<a, 1<500<b

# Rearranging a + b + c = 1000 gives c = 1000 - a - b
# Inserting that into a**2 + b**2 = c**2, then do a bit of algebra on paper, and we get this formula:
# b = (1000000 - (2000*a)) / (2000 - (2*a))

#Now we just have to check all the possible values of a, noting that we won't have to go beyond a = 333 as a < b < c (although the loop shouldn't get that far anyway so it doesn't really matter)
for a in range(1, 333):
    b = (1000000 - (2000*a)) / (2000 - (2*a))
    if int(b) == b: #No point calculating c if b isn't an integer
        c = 1000 - a - b
        print(f"a = {a}, b = {int(b)}, c = {int(c)}, so abc = {int(a*b*c)}")

