# https://codechalleng.es/bites/7/
"""Extract datetimes from log entries and calculate the time
   between the first and last shutdown events"""
from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
logfile = os.path.join("/tmp", "log")
urllib.request.urlretrieve("http://bit.ly/2AKSIbf", logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)"""
    datetime_str = line.split(" ")[1]
    date_str, time_str = datetime_str.split("T")
    year, month, day = map(int, date_str.split('-'))
    hour, minute, sec = map(int, time_str.split(':'))
    return datetime(year, month, day, hour, minute, sec)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object."""
    events = [' '.join(line.split(" ")[3:]).rstrip('.\n') for line in loglines]
    times = [convert_to_datetime(line) for line in loglines]
    shutdown_times = []
    for i, event in enumerate(events):
        if event == SHUTDOWN_EVENT:
            shutdown_times.append(times[i])
    return shutdown_times[-1] - shutdown_times[0]

# tests

def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    diff = time_between_shutdowns(loglines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'

if __name__ == '__main__':
    test_convert_to_datetime()
    test_time_between_events()