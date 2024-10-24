from grid import grid, grid_size

import numpy as np
import pandas as pd


def create_blank_matrix(size: int = grid_size) -> pd.DataFrame:
    return pd.DataFrame(
        index=range(size),
        columns=range(size)
        )


def convert_str_to_matrix(grid: str = grid) -> pd.DataFrame:
    matrix = create_blank_matrix()
    for i, row in enumerate(grid.splitlines()):
        for j in range(grid_size):
            matrix[i][j] = row[3*j:3*j+2]
    return matrix


def find_max_product(matrix: pd.DataFrame = convert_str_to_matrix()) -> int:
    max_product: int = 0
    # Row products
    # Col products
    # Diag products
    return max_product


find_max_product()
