'''Problem 4: Largest Palindrome Product

https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''


def is_palindrome(num: int) -> bool:
    '''Return True if num is a palindrome'''
    num_as_str = str(num)
    return (num_as_str == num_as_str[::-1])


print(is_palindrome(2003)) # expect False
print(is_palindrome(2002)) # expect True


def largest_palindromic_number(k: int) -> int:
    '''Return the largest palindromic number made from the product of 
    two numbers with k digits, and a list of the two numbers used'''
    largest_palindrome = 0
    product_nums = []
    for num_1 in range(10 ** (k - 1), 10 ** (k)):
        for num_2 in range(num_1, 10 ** (k)):
            if is_palindrome(num_1 * num_2) and num_1 * num_2 > largest_palindrome:
                largest_palindrome = num_1 * num_2
                product_nums = [num_1, num_2]
    return largest_palindrome, product_nums


print(largest_palindromic_number(2)) # expect (9009, [91, 99])
print(largest_palindromic_number(3))
print(largest_palindromic_number(4)) # bonus!
