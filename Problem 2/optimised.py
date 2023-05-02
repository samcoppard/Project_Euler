#Optimised solution from PE forums (slightly adjusted)

#Create variables to store the two most recently calculated Fib numbers
num1 = 1
num2 = 2

#Create a variable to store the sum of the even Fib numbers
total = 0

#Keep iterating until num1 exceeds 4 million
while num1 < 4000000:
  #Check if num1 is even, and add it to the running total if it is
  if num1 % 2 == 0:
    total += num1
  #Same for num2, but you've also got to check that num2 doesn't exceed 4 million (lots of the solutions in the forum don't run this check, as it works correctly for many max values, including 4 million, but that's just luck - the check is required for some larger values e.g. 60 million)
  if num2 % 2 == 0 and num2 < 4000000:
    total += num2
  #This is the clever bit. Add num2 to num1 to store the next Fib number (no need to store them all, just the most recent one, as you're summing them as you go)
  num1 += num2
  #And then add the new num1 to num2, to get the next Fib number without having to do another loop! Genius.
  num2 += num1

print(total)