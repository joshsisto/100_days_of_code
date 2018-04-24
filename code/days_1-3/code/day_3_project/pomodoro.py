

'''Pomodoro Timer
The Pomodoro timer is a well-known productivity interval that has been shown to improve your productivity.
It gives you a prescribed interval of 25 minutes of work followed by a 5-minute break. After 4 work intervals,
there is a 15-minute break. If you want to get started on a Pomodoro Timer, just click the Pomodoro button above.'''

'''A fun project would be to create yourself a Pomodoro Timer that incorporates datetime rather than just the time 
module. Have it display timestamps. This could also be applied to a stopwatch app. Use time of course but also 
throw in the timestamps and even some basic calculations on the difference between the start and end timestamps.'''

from datetime import date, timedelta
import time
import datetime

now = datetime.datetime.now().timestamp()

#t_now = timedelta.

#print(now)

ts = time.localtime()
#print(time.strftime("%Y-%m-%d %H:%M:%S", ts))


print(time.strftime("%x %X", ts))