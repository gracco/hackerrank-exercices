#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum_l = []
reve_sum_l = []
l = []

i = 0
i2 = n -1
for lists in a:
    for itens in lists:
        l.append(itens)

while i <= len(l):
    sum_l.append(l[i])
    i = (n + 1) + i


while i2 <= len(l) and len(reve_sum_l) < n:
    reve_sum_l.append(l[i2])
    i2 = (n - 1) + i2

num_a = sum(sum_l)
num_b = sum(reve_sum_l)


print(abs(sum(sum_l) - sum(reve_sum_l)))
