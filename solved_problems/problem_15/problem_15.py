'''Problem 15: Lattice Paths

https://projecteuler.net/problem=15

Starting in the top left corner of a 2 x 2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner (see grid.png).

How many such routes are there through a 20 x 20 grid?'''


# For a 2 x 2 grid, the 6 routes are RRDD, RDRD, RDDR, DRRD, DRDR, DDRR. Each route
# has exactly 2 moves right and 2 moves down.

# For a n x n grid, each route must have n moves right and n moves down. Hence the
# number of routes is simply the number of combinations of 2*n moves with exactly
# n moves right and n moves down, or equivalently the number of combinations of n 
# moves right in 2*n total moves. This is C(2*n, n) = (2n)! / (n!)**2. 


from math import factorial


def combination(n: int, r: int) -> int:
    '''Return the combination formula C(n, r) = n! / (r! * (n-r)!)'''
    return int(factorial(n) / (factorial(r) * factorial(n-r)))


def number_routes_through_grid(n: int) -> int:
    '''Return number of routes through n x n grid'''
    return combination(2*n, n)


print(number_routes_through_grid(n=2)) # expect 6
print(number_routes_through_grid(n=20))
