'''Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?'''


from problem_3 import prime_factor_decomposition


def lowest_common_multiple(nums: list[int]) -> int:
    '''Return the LCM of a list of integers'''
    prime_factor_lists: list[list[int]] = []
    lcm = 1
    for num in nums:
        prime_factor_lists.append(prime_factor_decomposition(num))
    for factor_list in prime_factor_lists:
        for factor in factor_list:
            lcm *= factor
            for pf_list in prime_factor_lists:
                if factor in pf_list:
                    pf_list.remove(factor)
    return lcm


print(lowest_common_multiple([1, 2, 3, 4, 5]))


def first_n_integers(n: int) -> list[int]:
    '''Return a list of the first n positive integers'''
    return range(1, n+1)


# Combine above functions to find the LCM of all numbers from 1 to 20
print(lowest_common_multiple(first_n_integers(10))) # expect 2520
print(lowest_common_multiple(first_n_integers(20)))
