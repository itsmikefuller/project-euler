'''Problem 7: 10001st Prime

https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?'''


from problem_3 import prime_factor_decomposition


def nth_prime(n: int) -> int:
    '''Return the nth prime number'''

    # Prime number position: kth prime number
    prime_number_position: int = 0
    
    # Test prime: number to test for primality
    test_prime: int = 0

    # Loop until nth prime found
    while prime_number_position < n:
        test_prime += 1
        if len(prime_factor_decomposition(test_prime)) == 1:
            prime_number_position += 1
    return test_prime


print(nth_prime(6)) # expect 13
print(nth_prime(10001))
