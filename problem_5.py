from problem_3 import prime_factor_decomposition


def lowest_common_multiple(nums: list[int]) -> int:
    prime_factor_lists: list[list[int]] = []
    lcm = 1
    for num in nums:
        prime_factor_lists.append(prime_factor_decomposition(num))
    for factor_list in prime_factor_lists:
        for factor in factor_list:
            lcm *= factor
            for list in prime_factor_lists:
                if factor in list:
                    list.remove(factor)
    return lcm

print(lowest_common_multiple([1, 2, 3, 4, 5]))


def first_n_integers(n: int) -> list[int]:
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list


print(lowest_common_multiple(first_n_integers(10)))
print(lowest_common_multiple(first_n_integers(20)))