#!/bin/python

import sys
n = int(raw_input().strip())
remainder=0
a=[]
count=0
countmax=0

while(n > 0):
    remainder = n%2;
    n = n/2;
    a=[remainder] + a

for i in range (a.__len__()):
    if a[i]==1:
        count=count+1
        countmax=max(count, countmax)
    else:
        count=0
        
print countmax

