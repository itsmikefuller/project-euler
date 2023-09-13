def is_palindrome(n: int) -> bool:
    str_n = str(n)
    return (str_n == str_n[::-1])

print(is_palindrome(2003))
print(is_palindrome(2002))


def largest_palindromic_number(digits=3):
    largest_palindrome = 0
    product_nums = []
    for num_1 in range(10 ** (digits - 1), 10 ** (digits)):
        for num_2 in range(num_1, 10 ** (digits)):
            if is_palindrome(num_1 * num_2) and num_1 * num_2 > largest_palindrome:
                largest_palindrome = num_1 * num_2
                product_nums = [num_1, num_2]
    return largest_palindrome, product_nums


print(largest_palindromic_number())
print(largest_palindromic_number(4)) # bonus!
