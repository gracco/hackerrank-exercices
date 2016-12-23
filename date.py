#!/bin/python3

import sys
import re

time = input().strip()
am_pm = re.search("AM",time)

time_list = time.split(':')
hour_time = int(time_list[0]) + 12
military_time_pm = time_list[2].replace('PM', '')
military_time_am = time_list[2].replace('AM', '')

if am_pm:
    if time_list[0] == '12' or time_list[0] == '24':
        print("{}:{}:{}".format('00',time_list[1],military_time_am))
    else:
        print("{}:{}:{}".format(time_list[0],time_list[1],military_time_am))
else:
    if time_list[0] == '12' or time_list[0] == '24':
        print("{}:{}:{}".format('12',time_list[1],military_time_pm))
    else:
        print("{}:{}:{}".format(hour_time,time_list[1],military_time_pm))
