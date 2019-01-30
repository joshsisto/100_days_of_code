import time
import datetime

l = [1, 3, 4]

print(str(l))

def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

get_timestamp()

print(type(get_timestamp()))