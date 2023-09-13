def sum_of_first_n_squares(n: int) -> int:
    return sum(i**2 for i in range(1, n+1))

def square_of_sum_of_first_n_ints(n: int) -> int:
    return sum(i for i in range(1, n+1)) ** 2

def sum_square_diff(n: int) -> int:
    return square_of_sum_of_first_n_ints(n) - sum_of_first_n_squares(n)

print(sum_square_diff(10))
print(sum_square_diff(100))