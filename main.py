#!/usr/bin/env python
import time

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    if sentence == "This sentence must be completed!!":
        print("Time:  %d.%d" % (mins, sec))
    else:
        print("Not correct!!")

input("Press enter to start")
start_time = time.time()

sentence = input("This sentence must be completed!!\n")
stop_time = time.time()

time = stop_time - start_time
time_convert(time)
