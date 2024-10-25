'''Problem 9: Special Pythagorean Triplet

https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which

a**2 + b**2 == c**2.

For example, 3**2 + 4**5 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.'''


def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    '''Return true if three integers a < b < c are a Pythagorean triple'''
    return (a** 2 + b ** 2 == c ** 2)


print(is_pythagorean_triple(3, 4, 5)) # expect True
print(is_pythagorean_triple(2, 5, 6)) # expect False


def pythag_triples_that_sum_to_n(n: int) -> list[tuple]:
    '''Return a list of Pythagorean triples that sum to n'''
    triples = []
    for a in range(1, n-1):
        for b in range(a, n-1-a):
            c = n - a - b
            if is_pythagorean_triple(a, b, c):
                triples.append((a, b, c))
    return triples


print(pythag_triples_that_sum_to_n(n=1000)) # expect only one tuple

# Return product abc
(a, b, c) = pythag_triples_that_sum_to_n(n=1000)[0]
print(a * b * c)
