from datetime import datetime
from datetime import timedelta
from time import sleep
import sys

WORK_TIME = 3  # Minutes
PLAY_TIME = 1  # Minutes
SLEEP_TIME = 5  # Seconds


def minutes_seconds(seconds):
    minutes = seconds // 60
    seconds = round(seconds - minutes * 60, 2)
    return (minutes, seconds)


def print_time_doing(seconds, activity):
    minutes, seconds = minutes_seconds(seconds)
    print(f"You've been {activity} for {minutes} minutes and {seconds} seconds!")


if __name__ == "__main__":

    start = datetime.now()
    work_time = timedelta(minutes=WORK_TIME)
    play_time = timedelta(minutes=PLAY_TIME)
    print(f"You started working at {start}")
    while start + work_time > datetime.now():
        print_time_doing((datetime.now() - start).seconds, "working")
        sleep(SLEEP_TIME)
    print("Party Time!")
    while start + work_time + play_time > datetime.now():
        print_time_doing((datetime.now() - start - work_time).seconds, "partying")
        sleep(SLEEP_TIME)
    print("All done!")
