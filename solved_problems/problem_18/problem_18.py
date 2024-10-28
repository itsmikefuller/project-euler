'''Problem 18: Maximum Path Sum I

https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row
below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every
route. However, Problem 67, is the same challenge with a triangle containing one-hundred
rows; it cannot be solved by brute force, and requires a clever method!'''


import pandas as pd

from triangles import small_triangle, large_triangle


def convert_triangle_str_to_dataframe(triangle: str) -> pd.DataFrame:
   '''Return a lower triangular DataFrame using a multiline string in the form of a triangle'''
   matrix = [line.split() for line in triangle.splitlines()]
   return pd.DataFrame(matrix).apply(pd.to_numeric)


# A route down the triangle is the same as a route down the DataFrame where the only admissible
# moves are left (i, j) -> (i+1, j) or right (i, j) -> (i+1, j+1).


def left(state: list[int]) -> list[int]:
   '''Return the state from a left move (i, j) -> (i+1, j)'''
   return [state[0]+1, state[1]]


def right(state: list[int]) -> list[int]:
   '''Return the state from a right move (i, j) -> (i+1, j+1)'''
   return [state[0]+1, state[1]+1]


from itertools import product


def all_routes_of_a_triangle(triangle: str) -> list[list]:
   '''Return a list of all routes of a triangle'''
   
   df = convert_triangle_str_to_dataframe(triangle)
   route_length = df.shape[0] - 1
   all_routes = product(*[['L', 'R']] * route_length)
   
   # Create list of numbers seen in each route
   all_routes_numbers = []
   for route in all_routes:
      current_state = [0, 0]
      route_numbers = [df.iloc[current_state[0], current_state[1]]]
      for turn in route:
         if turn == "L": current_state = left(current_state)
         if turn == "R": current_state = right(current_state)
         route_numbers.append(df.iloc[current_state[0], current_state[1]])
      all_routes_numbers.append(route_numbers)
   
   return all_routes_numbers


def max_total_of_all_routes(routes: list[list]) -> int:
   '''Return the largest total from a list of routes'''
   return max(sum(route) for route in routes)


def best_route(routes: list[list]) -> list[int]:
   '''Return the route that provides the largest total'''
   max_total = max_total_of_all_routes(routes)
   for route in routes:
      if sum(route) == max_total: return route


routes = all_routes_of_a_triangle(small_triangle)
print(max_total_of_all_routes(routes)) # expect 23
print(best_route(routes)) # expect [3, 7, 4, 9]


routes = all_routes_of_a_triangle(large_triangle)
print(max_total_of_all_routes(routes))
print(best_route(routes))
