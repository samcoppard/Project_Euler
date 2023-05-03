"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#The only change here is to stop searching for more palindromes when we're confident we've got the largest one

#Create a function to check if a number is a palindrome, by checking that each digit matches its opposite counterpart digit.
#If a digit doesn't match, we can stop checking straight away rather than wasting time checking the other digits.
def is_palindrome(num):
    a = str(num)
    return a == a[::-1]


#Create a list to store the palindromes we find (including the number 0 so that the max function that comes later always works)
palindromes = [0]

#Find palindromes by checking all x*y where min < x < max, y = min
#In this case, we're going to use this to set max = 999, so we calculate 999*999, then 999*998 and 998*998, then 999*997 and 998*997 and 997*997, etc etc
def find_palindromes(max, min):
    for i in range(max, min-1, -1):
        product = i * min
        #Check if the product is a palindrome, and add it to our list of palindromes if so
        if is_palindrome(product):
            palindromes.append(product)

#We need to look for palindromes that are the product of x*y, where 99 < x, y < 1000
#By starting at the top of the range, we can find the biggest palindromes fastest
for j in range(999, 99, -1):
    find_palindromes(999, j)
    #We might not find the biggest palindrome first, so we only stop searching when the largest palindrome we've found is bigger than any possible product left to check
    if max(palindromes) > 999 * (j-1):
        break

print(max(palindromes))