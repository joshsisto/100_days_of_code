#!python3

from datetime import datetime
from datetime import date

today = datetime.today()

today_date = date.today()

DOB = date(1989, 2, 2)

death_day = date(2075, 2, 2)

death_death = (death_day - DOB).days

days_alive = (today_date - DOB).days

print("datetime.today", today)
print("Today's date", today_date)
print("Date of birth", DOB)

print("Days left: ", death_death, "days, if I live to be 86")

print("Days here: ", days_alive, "days")

