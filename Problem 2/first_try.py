#The obvious first try is recursion, but that gets insanely computationally expensive very quickly

#Instead, let's put the first two Fibonacci numbers in a list
fib_series = [1, 2]

#Then we append each subsequent Fibonacci number to the list, which is speedy as we're storing each one in a list so they don't have to be re-calculated every time

#But we only want to go up to 4 million
while fib_series[-1] < 4000000:
  a = fib_series[-1] + fib_series[-2]
  if a < 4000000:
    fib_series.append(a)
  else:
    break

#Use a generator expression to chuck out the odd numbers and sum the even numbers that remain
even_fibs = sum(i for i in fib_series if i % 2 == 0)

print(even_fibs)