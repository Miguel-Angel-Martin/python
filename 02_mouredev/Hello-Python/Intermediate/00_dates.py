'''dates and time'''
# https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta


now = datetime.now()


def print_date(date_time):
    '''print data of the time'''
    print("Print the date from 1st function: ")
    print("Year:", date_time.year)
    print("Month:", date_time.month)
    print("Day:", date_time.day)
    print("Hour:", date_time.hour)
    print("Minute:", date_time.minute)
    print("Second:", date_time.second)
    print("TimeStamp:", date_time.timestamp())


print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time

print("Print the date from 2sd function: ")
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date

print("Print the date from 3rd function: ")
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# date operations

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
