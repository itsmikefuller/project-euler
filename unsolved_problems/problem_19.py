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
        self.test_date = (date, month, year)
        if self._admissible_date(self.test_date):
            self.date = self.test_date


    def _admissible_date(self) -> bool:
        date = self.test_date[0]
        month = self.test_date[1]
        year = self.test_date[2]

        if month not in range(1, 13):
            return False
        elif month in [4, 6, 9, 11] and date not in range(1, 31):
            return False
        elif month == 2 and self.is_leap_year(year) and date not in range(1, 30):
            return False
        elif month == 2 and not self.is_leap_year(year) and date not in range(1, 29):
            return False
        else:
            return True
            
        
    def is_leap_year(self, year: int) -> bool:
        if year % 4 == 0:
            if year % 400 == 0: return True
            elif year % 100 == 0: return False
            else: return True
        return False

    
    def next(self, date: tuple[int]) -> tuple[int]:
        date = self.test_date[0]
        month = self.test_date[1]
        year = self.test_date[2]

        if self._admissible_date((date + 1, month, year)):
            return (date + 1, month, year)
        elif self._admissible_date((1, month + 1, year)):
            return (1, month + 1, year)
        else:
            return (1, 1, year + 1)

    
    def is_sunday(self, date: tuple[int]) -> bool:
        if not self._admissible_date(date): 
            return False
        elif date == (1, 1, 1900): 
            return True
        
        counter = 0
        test_date = (1, 1, 1900)
        while test_date != date:
            counter += 1
            test_date = self.next(test_date)
        
        return (counter % 7 == 0)
