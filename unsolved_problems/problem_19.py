'''Problem 19: Counting Sundays

https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

days: list[str] = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]


class Date:
    def __init__(self,
                 date: int,
                 month: int,
                 year: int):
        if self.admissible_date((date, month, year)):
            self.date = (date, month, year)
            self.days = days

    
    # TODO: Fully build admissible_date function
    def admissible_date(self, test_date: tuple[int]) -> bool:
        date = test_date[0]
        month = test_date[1]
        year = test_date[2]

        # 1 <= date <= 31, 1 <= month <= 12
        if date not in range(1, 32) or month not in range(1, 13):
            return False
        
        # date special cases
        if month in [4, 6, 9, 11] and date not in range(1, 31):
            return False
