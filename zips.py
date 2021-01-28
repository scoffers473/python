#!/usr/bin/python

sunday = [10,10,10,9,8,8,9,10,11,12,13,13,18,22,20,19,19]
monday = [11,11,11,8,8,7,9,10,20,18,18,17,19,20,27,11,9]

for sun, mon  in zip(sunday, monday):
    print("Average=", (sun + mon ) / 2)
