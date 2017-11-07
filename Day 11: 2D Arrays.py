#!/bin/python

import sys


arr = []
s=0
maxs=0

for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

for row in xrange (4):
   for column in range (4):
      s=arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row+1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]
      maxs=max(s,maxs)

print maxs
