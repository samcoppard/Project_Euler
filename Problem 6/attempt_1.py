"""The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + ... + 10**2 == 385

The square of the sum of the first ten natural numbers is (1+2+...+10)**2 == 55**2 == 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 == 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

#The sum of an arithmetic sequence is (n/2)*(a+L) where n is the number of terms, a is the first number in the sequence, and L is the last number in the sequence
square_of_sum = ((100 / 2) * (1 + 100))**2 #This is O(1)

#Brute force for the sum of squares using a list comprehension. This is O(n)
sum_of_squares = sum([i**2 for i in range(1, 101)])

print(f"The difference is {int(square_of_sum - sum_of_squares)}")