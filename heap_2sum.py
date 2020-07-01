#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 01:26:47 2020

@author: xueqiwang
"""

f = open('algo1-programming_prob-2sum.txt')
lines = f.readlines()
f.close()

nums = dict()
for num in lines:
    num = int(num)
    key = num // 10000
    if key not in nums:
        nums[key] = dict()
    if num not in nums[key]:
        nums[key][num] = 1
    else:
        nums[key][num] += 1

get = dict()

for k1 in nums.keys():
    # avoid repeated computation
    if k1 > 0:
        continue
    for k2 in range(-k1-2, -k1+1):
        if k2 in nums.keys():
            for v1 in nums[k1].keys():
                for v2 in nums[k2].keys():
                    if (v1 == v2 and nums[k1][v1] >= 2) or (v1 != v2):
                        s = v1 + v2
                        if s >= -10000 and s <= 10000 and s not in get:
                            get[s] = True
print(len(get))