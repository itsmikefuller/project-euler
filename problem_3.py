def prime_factor_decomposition(n: int):
    prime_factors_of_n: list = []
    prime_factor_test = 2
    while prime_factor_test <= n:
        if n % prime_factor_test == 0:
            # print(f'{prime_factor_test} is a factor...')
            prime_factors_of_n.append(prime_factor_test)
            n /= prime_factor_test
        else:
            prime_factor_test += 1
    return prime_factors_of_n

# print(prime_factor_decomposition(13195))
# print(prime_factor_decomposition(600851475143))
