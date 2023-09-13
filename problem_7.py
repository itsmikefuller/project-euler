from problem_3 import prime_factor_decomposition


def nth_prime(n: int) -> int:
    list_of_primes = []
    i = 2
    while len(list_of_primes) < n:
        if len(prime_factor_decomposition(i)) == 1:
            list_of_primes.append(i)
        i += 1
    return list_of_primes[-1]

print(nth_prime(6))
print(nth_prime(10001))