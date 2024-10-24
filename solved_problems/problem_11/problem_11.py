'''Problem 11: Largest Product in a Grid

https://projecteuler.net/problem=11

In the 20 x 20 grid (see grid.py), four numbers along a diagonal line in the rough
centre of the grid (starting line 7) multiply to make 26 * 63 * 78 * 14 = 1788696. [sic]

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the grid?'''


from math import prod

from grid import grid, grid_size

import pandas as pd


class Solution:
    def __init__(
            self,
            grid: str,
            grid_size: int,
            length: int
        ):
        self.grid = grid
        self.grid_size = grid_size
        self.length = length
        self.matrix = self.convert_str_to_matrix()


    def convert_str_to_matrix(self) -> pd.DataFrame:
        '''Convert self.grid, a multiline string of two-digit numbers, to a dataframe'''
        matrix = pd.DataFrame(index=range(self.grid_size), columns=range(self.grid_size))
        for i, row in enumerate(self.grid.splitlines()):
            for j in range(self.grid_size):
                matrix[i][j] = int(row[3*j:3*j+2])
        return matrix


    def greatest_row_product(self, matrix: pd.DataFrame) -> int:
        '''Return the greatest product of k adjacent numbers in a matrix (horizontally
        only), where k = length'''
        greatest_row_product: int = 0
        greatest_product_components: list[int] = []
        for _, row in matrix.iterrows():
            for j in range(self.grid_size - self.length + 1):
                product = prod(row[i] for i in range(j, j + self.length))
                if product > greatest_row_product: 
                    greatest_row_product = product
                    greatest_product_components = [row[i] for i in range(j, j + self.length)]
        print(greatest_product_components)
        return greatest_row_product


    def greatest_southeast_diag_product(self, matrix: pd.DataFrame) -> int:
        '''Return the greatest product of k adjacent numbers in a matrix (diagonally
        only), where k = length. Considers only "southeast" diagonals, where both row and 
        column indices increase from a starting point, e.g. (i, j), (i+1, j+1), (i+2, j+2)...'''
        greatest_diag_product: int = 0
        greatest_product_components: list[int] = []
        for i in range(self.grid_size - self.length + 1):
            for j in range(self.grid_size - self.length + 1):
                product = prod(matrix.iloc[i+k][j+k] for k in range(self.length))
                if product > greatest_diag_product:
                    greatest_diag_product = product
                    greatest_product_components = [matrix.iloc[i+k][j+k] for k in range(self.length)]
        print(greatest_product_components)
        return greatest_diag_product


    def find_greatest_product(self) -> int:
        '''Return the greatest product of k adjacent numbers in a square matrix (horizontally,
        vertically, or diagonally), where k = length'''
        
        # Row products: for each row, compute products and update largest product when found
        max_row_product = self.greatest_row_product(matrix=self.matrix)
        print(f"Greatest row product: {max_row_product}")
        
        # Col products: transpose matrix and re-run row product function
        max_col_product = self.greatest_row_product(matrix=self.matrix.transpose())
        print(f"Greatest col product: {max_col_product}")
        
        # "Southeast" diagonal products: find maximum diagonal product where row/col indices increase
        max_southeast_diag_product = self.greatest_southeast_diag_product(matrix=self.matrix)
        print(f"Greatest southeast diag product: {max_southeast_diag_product}")

        # "Southwest" diagonal products: reverse rows of matrix and re-run southeast product function
        max_southwest_diag_product = self.greatest_southeast_diag_product(matrix=self.matrix.iloc[::-1])
        print(f"Greatest southwest diag product: {max_southwest_diag_product}")

        return max(max_row_product, max_col_product, max_southeast_diag_product, max_southwest_diag_product)


solution = Solution(
    grid=grid,
    grid_size=grid_size,
    length=4
)
print(f'Overall greatest product of {solution.length} adjacent numbers: {solution.find_greatest_product()}')


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
Overall greatest product of 4 adjacent numbers: 70600674
'''
