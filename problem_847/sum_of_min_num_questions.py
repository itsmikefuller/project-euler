from min_num_questions import min_num_questions_given_plates


def sum_of_min_num_questions(N: int, debug:bool = False) -> int:
    result = 0
    for a in range(0, N+1):
        for b in range(0, N+1-a):
            for c in range(0, N+1-a-b):
                if a + b + c != 0:
                    result += min_num_questions_given_plates(a, b, c)
                    if debug:
                        print(f'(a, b, c): ({a}, {b}, {c})     h(a, b, c) = {min_num_questions_given_plates(a, b, c)}      subtotal = {result}')
    return result