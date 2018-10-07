from datetime import datetime
from datetime import timedelta
from time import sleep
import sys

WORK_TIME = 3  # Minutes
PARTY_TIME = 1  # Minutes
SLEEP_TIME = 5  # Seconds


def minutes_seconds(seconds):
    minutes = seconds // 60
    seconds = round(seconds - minutes * 60, 2)
    return (minutes, seconds)


def print_time_doing(seconds, activity):
    minutes, seconds = minutes_seconds(seconds)
    print(f"You've been {activity} for {minutes} minutes and {seconds} seconds!")


def pomodoro(work_time=WORK_TIME, party_time=PARTY_TIME):
    start = datetime.now()
    _work_time = timedelta(minutes=work_time)
    _party_time = timedelta(minutes=party_time)
    print(f"You started working at {start}")
    while start + _work_time > datetime.now():
        print_time_doing((datetime.now() - start).seconds, "working")
        sleep(SLEEP_TIME)
    print("Party Time!")
    while start + _work_time + _party_time > datetime.now():
        print_time_doing((datetime.now() - start - _work_time).seconds, "partying")
        sleep(SLEEP_TIME)
    print("All done!")


if __name__ == "__main__":
    # Command line options: pomodoro <work time> <party time> <repeat number>
    # If no commands, or too many, use default values and only repeat once

    if len(sys.argv) != 4:
        print("Using default settings")
        pomodoro()
    else:
        work_time, party_time, n = map(int, sys.argv[1:])
        print(f"Work for {work_time} minutes and party for {party_time} minutes")
        print(f"Repeat {n} times")
        for _ in range(n):
            pomodoro(work_time, party_time)

