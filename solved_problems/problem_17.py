'''Problem 17: Number Letter Counts

https://projecteuler.net/problem=17


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with 
British usage.'''


# My code below can return word forms of numbers far beyond 1000, going up to 
# 10**15 - 1. It can be easily extended by adding to the block_indices dictionary.


# Word forms of numbers can be described in blocks of 3 place values: e.g. 
# 1 223 449 is three blocks: (one million), (two hundred and twenty-three
# thousand), (four hundred and forty-nine). Hence we start by building a function
# to determine the word form of a three-digit number input (which itself can be
# broken down into the hundreds digit and tens/units digits), and use it in a
# function to return the word form of higher digit numbers.


units: dict = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
tens: dict = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
multiples_of_ten: dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}
block_indices: dict = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion"
}


def two_digit_number_in_words(num: int) -> str:
    '''Return the word form of a number up to two digits'''
    if len(str(num)) == 1: 
        return units[str(num)]
    if len(str(num)) == 2 and int(str(num)[0]) == 1: 
        return tens[str(num)]
    if len(str(num)) == 2 and int(str(num)[0]) != 1: 
        return multiples_of_ten.get(str(num)[0]) + " " + units.get(str(num)[1])


def three_digit_number_in_words(num: int) -> str:
    '''Return the word form of a number up to three digits'''
    if len(str(num)) != 3:
        return two_digit_number_in_words(num)
    if len(str(num)) == 3 and int(str(num)[1:]) == 0:
        return units[str(num)[0]] + " hundred"
    if len(str(num)) == 3 and int(str(num)[1:]) != 0:
        return units[str(num)[0]] + " hundred and " + two_digit_number_in_words(int(str(num)[1:]))


def number_in_words(num: int) -> str:
    '''Return the word form of num'''
    
    # Prepare blocks: e.g. if num = 1 223 449, then blocks = [1, 223, 449]
    blocks = []
    while num:
        block_size = min(3, len(str(num)))
        block = int(str(num)[-block_size:])
        blocks.insert(0, block)
        num = int(str(num)[:-block_size] or 0)
    
    # Form word per block
    word = ''
    for index, block in enumerate(blocks):
        block_index = len(blocks) - index - 1
        word += three_digit_number_in_words(block) + f' {block_indices[block_index]} '
    
    return word


print(number_in_words(123)) # expect "one hundred and twenty three"
print(number_in_words(1223449)) # expect "one million two hundred and twenty three thousand four hundred and forty nine


def number_of_letters(num: int) -> int:
    '''Return the total number of letters used in the word form of num'''
    return len(number_in_words(num).replace(" ", ""))


def total_number_of_letters(start: int, finish: int) -> int:
    '''Return the total number of letters used in the word form of all numbers
    between start and finish (inclusive)'''
    return sum(number_of_letters(i) for i in range(start, finish + 1))


print(total_number_of_letters(start=1, finish=5)) # expect 19
print(total_number_of_letters(start=1, finish=1000))
