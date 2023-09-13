def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def answer():
    n = 0
    sum = 0
    while fib(n) <= 4000000:
        if fib(n) % 2 == 0:
            print(f'{n}th Fibonacci number, {fib(n)}, is even...')
            sum += fib(n)
        n += 1
    return sum

print(answer())