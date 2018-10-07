from datetime import datetime
from datetime import timedelta
from time import sleep
import sys

start = datetime.now()
work_time = timedelta(minutes=1)
play_time = timedelta(minutes=1)
print(f"You started working at {start}")
while start + work_time > datetime.now():
    print(f"You've been working for {(datetime.now()-start).seconds/60} minutes!")
    sleep(1)
print("Party Time!")
while start + work_time + play_time > datetime.now():
    print(
        f"You've been playing for {(datetime.now()-work_time-start).seconds/60} minutes!"
    )
print("All done!")
