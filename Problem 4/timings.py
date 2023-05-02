"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import timeit

attempt_1_code = """
def is_palindrome(num):
    for i in range(int(len(str(num))/2) + 1):
        if str(num)[i] != str(num)[-(i+1)]:
            return False
    return True

palindromes = [0]

def find_palindromes(max, min):
    for i in range(max, min-1, -1):
        product = i * min
        # Check if the product is a palindrome, and add it to our list of palindromes if so
        if is_palindrome(product):
            palindromes.append(product)

for j in range(999, 99, -1):
    find_palindromes(999, j)

print(max(palindromes))
"""

attempt_2_code = """
def is_palindrome(num):
    for i in range(int(len(str(num))/2) + 1):
        if str(num)[i] != str(num)[-(i+1)]:
            return False
    return True

palindromes = [0]

def find_palindromes(max, min):
    for i in range(max, min-1, -1):
        product = i * min
        # Check if the product is a palindrome, and add it to our list of palindromes if so
        if is_palindrome(product):
            palindromes.append(product)

for j in range(999, 99, -1):
    find_palindromes(999, j)
    if max(palindromes) > 999 * (j-1):
        break

print(max(palindromes))
"""

attempt_1_time = timeit.timeit(attempt_1_code, number=10)/10
attempt_2_time = timeit.timeit(attempt_2_code, number=10)/10

print("The code from my 1st attempt ran in {:.6f}s".format(attempt_1_time))
print("The code from my 2nd attempt ran in {:.6f}s".format(attempt_2_time))

improvement = attempt_1_time / attempt_2_time

print("The 2nd attempt was {:.2f}x faster".format(improvement))