"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

#Solved this one by hand:
#The solution will be the product of the lowest / smallest set of primes whose products include all the numbers from 2 to 20

#Test case:
#2*2*2*3*3*5*7 = 2520
#1,2,3,5,7 are trivial
#4 = 2*2
#6 = 2*3
#8 = 2*2*2
#9 = 3*3
#10 = 2*5
#So all numbers from 1 to 10 can be made from the given set of primes, but it wouldn't work if you removed any of those primes

#Solution:
#For the question, the smallest set of primes whose products include all the numbers from 2 to 20 is {2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19}

solution = 2*2*2*2*3*3*5*7*11*13*17*19

print(solution)