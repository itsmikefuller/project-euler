'''Problem 16: Power Digit Sum

https://projecteuler.net/problem=16


2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?'''


def sum_of_digits(num: int) -> int:
    return sum(int(digit) for digit in str(num))


print(sum_of_digits(2**15)) # expect 26
print(sum_of_digits(2**1000))
