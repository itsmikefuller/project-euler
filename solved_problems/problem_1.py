'''Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''


def is_multiple_of_3_or_5(num: int) -> bool:
    '''Return True if num is multiple of 3 or 5'''
    return True if (num % 3 == 0 or num % 5 == 0) else False


def sum_multiples_of_3_or_5(max_int: int) -> int:
    '''Return sum of all multiples of 3 or 5 below max_int'''
    answer = 0
    for i in range(max_int):
        if is_multiple_of_3_or_5(i): answer += i
    return answer


print(sum_multiples_of_3_or_5(10)) # expect 23
print(sum_multiples_of_3_or_5(1000))
