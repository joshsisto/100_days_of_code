
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = r'C:\Users\jsistox\PycharmProjects\create_trk\venv\tmp\log.txt'
#logfile = os.path.join('/tmp', 'log')
#urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
with open(logfile) as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    for log_line in line:
        words = log_line.split()
        words[1] = datetime.strptime(words[1], '%Y-%m-%dT%H:%M:%S')
        print(words[1])
        print(type(words[1]))
    pass

#convert_to_datetime(loglines)

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    for line in loglines:
        words = line.split()
        words_list = []
        if str(words[-2:]) == r"['Shutdown', 'initiated.']":
            words_list.append(line)
            #print(str(words[-2:]))
            #print(words_list)
            print(words_list)

        #print(str(words[-2:]))

    pass

time_between_shutdowns(loglines)
