'''
https://www.youtube.com/watch?v=pxe13_562Vs

Create folders with the mane of the months
'''

import calendar
from calendar import monthrange
from pathlib import Path
import datetime

year = (datetime.date.today()).year
year_months = list(calendar.month_name[1:])
files_dir = Path.cwd() / "calendar"
"./calendar"
for i, month in enumerate(year_months, 1):
    days = monthrange(year, i)[-1]
    for day in range(days):
        Path(
            f'calendar/{i}.{year}/{month}/Day-{day}').mkdir(parents=True, exist_ok=True)
