'''Problem 14: Longest Collatz Sequence

https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3*n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13, 40, 20, 10, 5, 16, 8, 4, 2, 1 

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''


def collatz_sequence(n: int) -> list[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence


def longest_chain(limit: int) -> int:
    
    print(f'Finding longest Collatz chain for starting number under {limit}...')
    
    longest_chain: list[int] = [] # capture longest Collatz chain
    longest_chain_length: int = 0 # capture chain length
    longest_chain_starting_number: int = 0 # capture corresponding starting number
    
    # Brute force loop - optimisation needed (hash map, store sequences and add to length if found?)
    for i in range(1, limit):
        test_chain = collatz_sequence(i)
        if len(test_chain) > longest_chain_length:
            longest_chain = test_chain
            longest_chain_length = len(test_chain)
            longest_chain_starting_number = i
        if i % 1e5 == 0: print(f'Tested {i} numbers. Longest Collatz chain currently found at starting number {longest_chain_starting_number}, with length {longest_chain_length}')
    print(f'Longest Collatz chain for starting number under {limit} has length {longest_chain_length}, with starting number {longest_chain_starting_number}')
    return longest_chain


print(collatz_sequence(13)) # expect [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
longest_chain(1000000)
