#!/usr/bin/python3
"""
This take an input number and works out the offset day based on this number

Days are Mon:1
         Tue:2
         Wed:3
         Thu:4
         Fri:5
         Sat:6
         Sun:7

So if i passwd an offset of 7 this would be a Sunday, a 5 a Friday, a 13 a Saturday, etc
"""

import sys

def solution  (D,S):

    # define tuple array - use day as day-1 so that it works easily with the modulus
    days = ([0,"Sun"],[1,'Mon'],[2,"Tue"],[3,"Wed"],[4,"Thu"],[5,"Fri"],[6,"Sat"])

   # Work out which day equates to this
    which_day = S % 7
    newday=0


    # Find the starting day Integer
    # (If Sun, add 7)
    # Then add the day offset and get the modulus
    # in order to determine the final day
    for day in days:
        if day[1] == D:
            starting_day = day[0]
            if starting_day == 0:
                starting_day = 7
            which_day = (S+starting_day)%7
            break

    # Now we have the final day, work out the day name
    for day in days:
        if day[0] == which_day:
            return day[1]

def main (D,S):
    ans = solution(D,S)
    print(ans)


if __name__ == "__main__":
    main(sys.argv[1],int(sys.argv[2]))

