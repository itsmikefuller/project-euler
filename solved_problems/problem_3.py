'''Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?'''


def prime_factor_decomposition(num: int) -> list[int]:
    '''Return list of prime factors of num'''
    prime_factors_of_num: list = []
    prime_factor_test = 2
    while prime_factor_test <= num:
        if num % prime_factor_test == 0:
            # print(f'{prime_factor_test} is a factor...')
            prime_factors_of_num.append(prime_factor_test)
            num /= prime_factor_test
        else:
            prime_factor_test += 1
    return prime_factors_of_num


print(prime_factor_decomposition(13195)) # expect [5, 7, 13, 29]
print(prime_factor_decomposition(600851475143))
