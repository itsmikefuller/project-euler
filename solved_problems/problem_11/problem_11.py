'''Problem 11: Largest Product in a Grid

https://projecteuler.net/problem=11

In the 20 x 20 grid (see grid.py), four numbers along a diagonal line in the rough
centre of the grid (starting line 7) multiply to make 26 * 63 * 78 * 14 = 1788696. [sic]

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the grid?'''


from math import prod

from grid import grid, grid_size

import pandas as pd


def convert_str_to_matrix(grid: str, grid_size: int) -> pd.DataFrame:
    '''Convert grid, a multiline string of two-digit numbers, to a dataframe'''
    matrix = pd.DataFrame(index=range(grid_size), columns=range(grid_size))
    for i, row in enumerate(grid.splitlines()):
        for j in range(grid_size):
            matrix[i][j] = int(row[3*j:3*j+2])
    return matrix


def greatest_row_product(matrix: pd.DataFrame, matrix_size: int, length: int) -> int:
    '''Return the greatest product of k adjacent numbers in a matrix (horizontally
    only), where k = length'''
    greatest_row_product: int = 0
    greatest_product_components: list[int] = []
    for _, row in matrix.iterrows():
        for j in range(matrix_size - length + 1):
            product = prod(row[i] for i in range(j, j+length))
            if product > greatest_row_product: 
                greatest_row_product = product
                greatest_product_components = [row[i] for i in range(j, j+length)]
    print(greatest_product_components)
    return greatest_row_product


def greatest_southeast_diag_product(matrix: pd.DataFrame, matrix_size: int, length: int) -> int:
    '''Return the greatest product of k adjacent numbers in a matrix (diagonally
    only), where k = length. Considers only "southeast" diagonals, where both row and 
    column indices increase from a starting point, e.g. (i, j), (i+1, j+1), (i+2, j+2)...'''
    greatest_diag_product: int = 0
    greatest_product_components: list[int] = []
    for i in range(matrix_size - length + 1):
        for j in range(matrix_size - length + 1):
            product = prod(matrix.iloc[i+k][j+k] for k in range(length))
            if product > greatest_diag_product: 
                greatest_diag_product = product
                greatest_product_components = [matrix.iloc[i+k][j+k] for k in range(length)]
    print(greatest_product_components)
    return greatest_diag_product


def find_greatest_product(matrix: pd.DataFrame, length: int) -> int:
    '''Return the greatest product of k adjacent numbers in a square matrix (horizontally,
    vertically, or diagonally), where k = length'''
    
    # Check matrix is square, get matrix size
    assert(matrix.shape[0] == matrix.shape[1])
    matrix_size: int = matrix.shape[0]
    
    # Row products: for each row, compute products and update largest product when found
    max_row_product = greatest_row_product(matrix=matrix, matrix_size=matrix_size, length=length)
    print(f"Greatest row product: {max_row_product}")
    
    # Col products: transpose matrix and re-run row product function
    max_col_product = greatest_row_product(matrix=matrix.transpose(), matrix_size=matrix_size, length=length)
    print(f"Greatest col product: {max_col_product}")
    
    # "Southeast" diagonal products: find maximum diagonal product where row/col indices increase
    max_southeast_diag_product = greatest_southeast_diag_product(matrix=matrix, matrix_size=matrix_size, length=length)
    print(f"Greatest southeast diag product: {max_southeast_diag_product}")

    # "Southwest" diagonal products: reverse rows of matrix and re-run southeast product function
    max_southwest_diag_product = greatest_southeast_diag_product(matrix=matrix.iloc[::-1], matrix_size=matrix_size, length=length)
    print(f"Greatest southwest diag product: {max_southwest_diag_product}")

    return max(max_row_product, max_col_product, max_southeast_diag_product, max_southwest_diag_product)


matrix = convert_str_to_matrix(grid=grid, grid_size=grid_size)
print(f'Answer: {find_greatest_product(matrix=matrix, length=4)}')


'''
Results:

[66, 91, 88, 97]
Greatest row product: 51267216
[78, 78, 96, 83]
Greatest col product: 48477312
[94, 99, 71, 61]
Greatest southeast diag product: 40304286
[89, 94, 97, 87]
Greatest southwest diag product: 70600674
Answer: 70600674
'''
