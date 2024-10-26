'''Problem 13: Large Sum

https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.'''


from numbers import numbers


'''A note on code performance: 

We don't need to sum 50-digit numbers here, just the 11-digit numbers comprised of the first
11 digits of each 50-digit number. Why?

Sketch proof: Let n_1, n_2, ..., n_100 be the 50-digit numbers to add. Naively, let's assume we
get the same first 10 digits of sum(n_i) by summing 100 10-digit numbers equal to the first 10
digits of each 50-digit number. Break each n_i into two components, F_i and l_i, where

F_i = (n_i - l_i), i.e. 50-digit number where the first 10 digits are the same as n_i, other digits 0,

l_i = (n_i %% 10**39), i.e. the 40-digit number comprised of the last 40 digits of n_i.

Then sum(n_i) = sum(F_i) + sum(l_i). Note that sum(n_i) in [100 * min(n_i), 100 * max(n_i)], 
so sum(n_i) is exactly 52 digits long. Similarly, sum(l_i) is exactly 42 digits long, and sum(F_i) is
exaclty 52 digits long but the first 12 digits are the only possible non-zero digits.

When sum(l_i) is added to sum(F_i), the first 10 digits do not change UNLESS there is a carry-over in
the 11th digit. That is, if any of the first 10 digits change, it can only be the 10th.

If we repeat the logic above, but break up the n_i into F_i and l_i considering the first (10+1)
digits, we won't run into a problem in the 10th digit.

This can be generalised: for any n, if we are summing 10**n numbers with N-digits, the first k digits
of the sum are the same as in the sum of the numbers comprised of the first (k+1) digits of each
N-digit number.'''


class Solution:
    def __init__(
        self,
        first_k_digits: int,
        numbers_string: str
    ):
        self.first_k_digits = first_k_digits
        self.numbers: list[int] = self.truncate_nums_in_multiline_string(numbers_string)


    def truncate_nums_in_multiline_string(self, string: str) -> int:
        '''Return list of numbers from numbers_string, only the first (k+1) digits'''
        return [int(num[:self.first_k_digits + 1]) for num in string.splitlines()]


    def first_k_digits_of_sum(self) -> str:
        '''Return first k digits of the sum of the numbers'''
        return str(sum(self.numbers))[:self.first_k_digits]


solution = Solution(
    first_k_digits=10,
    numbers_string=numbers
)
print(solution.first_k_digits_of_sum())
