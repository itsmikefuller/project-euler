def sum_primes_below_n(n: int) -> int:
    
    sum = 0
    is_prime: list[bool] = [True] * (n+1)

    for test_prime in range(2, n):
        if is_prime[test_prime]:
            sum += test_prime
            for i in range(test_prime ** 2, n, test_prime):
                is_prime[i] = False
    
    return sum

print(sum_primes_below_n(10))
print(sum_primes_below_n(10000))
print(sum_primes_below_n(2000000))


# The below code is O(n**2) time complexity which made it too long to run for n=2000000

# def is_prime(n: int) -> bool:
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(6))
# print(is_prime(997))


# def sum_primes_below_n(n: int) -> int:
#     primes = []
#     for num in range(2, n):
#         if is_prime(num):
#             primes.append(num)

#         if num % 10000 == 0:
#             print(f'Testing number {num}/{n}...')
#     return sum(prime for prime in primes)

# print(sum_primes_below_n(10))
# print(sum_primes_below_n(10000))
# print(sum_primes_below_n(2000000))

