"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Calculated by hand.

# There are only 30 constituent parts (the numbers 1, 2, ..., 20), the other basic 
# multiples of 10 (30, 40, ..., 90), plus the words "hundred", "thousand", and "and".

# Then it's just a case of putting them together into sensible groups and adding the
# totals together.
# 
# The final solution is 21124.