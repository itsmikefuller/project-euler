from min_num_questions import min_num_questions_given_plates
from sum_of_min_num_questions import sum_of_min_num_questions


def test(bool):
    try:
        assert bool
        print('Pass')
    except AssertionError:
        print('*FAIL*')


def test_min_num_questions_given_plates():

    print('Test function h(1, 2, 3) = 3:', end=" ")
    test(min_num_questions_given_plates(1, 2, 3) == 3)

    print('Test function h(2, 3, 3) = 3:', end=" ")  
    test(min_num_questions_given_plates(2, 3, 3) == 4)

    print('Test function h(4, 5, 5) = 5:', end=" ")  
    test(min_num_questions_given_plates(4, 5, 5) == 5)

    print('Test function h(0, 1, 1) = 1:', end=" ")
    test(min_num_questions_given_plates(0, 1, 1) == 1)

    print('Test function h(0, 5, 2) = 4:', end=" ")
    test(min_num_questions_given_plates(0, 5, 2) == 4)

    print('Test function h(0, 0, 1) = 0:', end=" ")
    test(min_num_questions_given_plates(0, 0, 1) == 0)

    return


def test_sum_of_min_num_questions(debug: bool):

    print('Test function H(6) = 203:')
    test(sum_of_min_num_questions(6, debug) == 203)

    # print('Test function H(20) = 7718:')
    # test(sum_of_min_num_questions(20, debug) == 7718)

    return