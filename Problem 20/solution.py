""" Find the sum of the digits in the number 100! """


def factorial(n) -> int:
    """Calculates n! for positive integer values of n"""
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def sum_of_digits(num) -> int:
    """Calculate the sum of the digits of a positive integer"""
    return sum([int(x) for x in str(num)])


print(f"The sum of the digits of 100! is {sum_of_digits(factorial(100))}")
