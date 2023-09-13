def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    return True if (a** 2 + b ** 2 == c ** 2) else False

print(is_pythagorean_triple(3, 4, 5))


def pythag_triples_that_sum_to_n(n: int) -> list[tuple]:
    triples = []
    for a in range(1, n-1):
        for b in range(a, n-1-a):
            c = n - a - b
            if is_pythagorean_triple(a, b, c):
                triples.append((a, b, c))
    return triples

print(pythag_triples_that_sum_to_n(n=1000)) # confirm only one tuple


(a, b, c) = pythag_triples_that_sum_to_n(n=1000)[0]
print(a * b * c)