# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __number_of_days_in_month(self, year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31

        if month != 2:
            return 30

        if year % 4 != 0:
            return 28

        if year % 400 == 0:
            return 29

        if year % 100 == 0:
            return 28

        return 29

    def add_7_days(self):
        self.day = self.day + 7

        nr_of_days_in_month = self.__number_of_days_in_month(
            self.year, self.month)
        if self.day > nr_of_days_in_month:
            self.month += 1
            self.day -= nr_of_days_in_month

            if self.month > 12:
                self.year += 1
                self.month = 1

    def is_after(self, year, month, day):
        if year < self.year:
            return True
        if year > self.year:
            return False

        if month < self.month:
            return True
        if month > self.month:
            return False

        return day < self.day

    def __str__(self):
        return str(self.year)+"."+str(self.month)+"."+str(self.day)


my_day = MyDate(1901, 1, 6)

count = 0

while my_day.is_after(2000, 12, 31) == False:
    my_day.add_7_days()

    if my_day.day == 1:
        count += 1
        print(my_day)

print(count)
