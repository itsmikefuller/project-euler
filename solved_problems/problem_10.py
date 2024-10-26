'''Problem 10: Summation of Primes

https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''


def sum_primes_below_n(n: int) -> int:
    '''Return the sum of all prime numbers below n'''

    sum = 0
    is_prime: list[bool] = [True] * (n+1)

    for test_prime in range(2, n):
        if is_prime[test_prime]:
            sum += test_prime
            # Mark all multiples of test_prime as not prime
            for i in range(2 * test_prime, n, test_prime): is_prime[i] = False
    
    return sum


print(sum_primes_below_n(10)) # expect 17
print(sum_primes_below_n(10000)) # bonus!
print(sum_primes_below_n(2000000))
