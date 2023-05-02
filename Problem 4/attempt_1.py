"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Create a function to check if a number is a palindrome, by checking that each digit matches its opposite counterpart digit.
# If a digit doesn't match, we can stop checking straight away rather than wasting time checking the other digits.


def is_palindrome(num):
    for i in range(int(len(str(num))/2) + 1):
        if str(num)[i] != str(num)[-(i+1)]:
            return False
    return True


# Create a list to store the palindromes we find (including the number 0 so that the max function that comes later always works)
palindromes = [0]

# Find palindromes by checking all x*y where min < x < max, y = min
# In this case, we're going to use this to set max = 999, so we calculate 999*999, then 999*998 and 998*998, then 999*997 and 998*997 and 997*997, etc etc


def find_palindromes(max, min):
    for i in range(max, min-1, -1):
        product = i * min
        # Check if the product is a palindrome, and add it to our list of palindromes if so
        if is_palindrome(product):
            palindromes.append(product)


# We need to look for palindromes that are the product of x*y, where 99 < x, y < 1000
# By starting at the top of the range, we can find the biggest palindromes fastest
for j in range(999, 99, -1):
    find_palindromes(999, j)

print(max(palindromes))
