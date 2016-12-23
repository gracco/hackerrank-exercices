#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a_list = [a0,a1,a2]
b_list = [b0,b1,b2]

a_score = 0
b_score = 0

for i in range(len(a_list)):
    if a_list[i] > b_list[i]:
        a_score += 1
    if a_list[i] < b_list[i]:
        b_score += 1
print("{} {}".format(a_score, b_score))
