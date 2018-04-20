#!python3

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

tt = timedelta(seconds=5.5)

print(t)

print(tt)

print(t.days)

print(t.seconds)
#Notice seconds only displays 10 hours in seconds


#create hours | seconds, minutes, hours
t.seconds / 60 / 60

t.seconds / 3600

eta = timedelta(hours=6)

today = datetime.today()

print(today)

print(today + eta)

print(str(today + eta))
