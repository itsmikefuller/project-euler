'''Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is

1**2 + 2**2 + ... + 10**2 = 385.

The square of the sum of the first ten natural numbers is

(1 + 2 + ... + 10)**2 = 55**2 = 3025.

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.'''


def sum_of_first_n_squares(n: int) -> int:
    '''Return the sum of the first n square numbers'''
    # return sum(i**2 for i in range(1, n+1))
    return n * (n+1) * (2*n + 1) / 6


def square_of_sum_of_first_n_ints(n: int) -> int:
    '''Return the square of the sum of the first n positive integers'''
    # return sum(i for i in range(1, n+1)) ** 2
    return n**2 * (n+1)**2 / 4


def sum_square_diff(n: int) -> int:
    '''Return (sum of first n squares) - (square of sum of first n integers)'''
    return square_of_sum_of_first_n_ints(n) - sum_of_first_n_squares(n)


print(sum_square_diff(10)) # expect 2640
print(sum_square_diff(100))
