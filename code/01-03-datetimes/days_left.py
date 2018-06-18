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



def death_clock():
    DOB_input = input('What is your date of birth?\n Format YYYY-MM-DD\n').split("-")
    DOB = []
    for num in DOB_input:
        DOB.append(int(num))
    DOB = date(DOB[0], DOB[1], DOB[2])
    years_left = input("How many years do you estimate you have left?\n")
    death_day = DOB.replace(DOB.year + int(years_left))
    death_death = (death_day - DOB).days
    print(f'\nYou estimate that you have {death_death} days left.')


death_clock()

