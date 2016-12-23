#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = []
negative = []
zero = []
for i in range(n):
    if arr[i] == 0:
        zero.append(arr[i])
    elif arr[i] > 0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])

print(float(len(positive)/n))
print(float(len(negative)/n))
print(float(len(zero)/n))
