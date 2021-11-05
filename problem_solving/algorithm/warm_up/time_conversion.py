# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# --> split as [hh, mm, ss], [AM] --> 


def timeConversion(s):
    period = str("".join(re.split("[^a-zA-Z]*", s))) # period = 'PM'
    print(period)
    s = s.replace(period, '')  # '07:05:45'
    print(s)
    s = s.split(':') # ['07', '05', '45']
    print(s)
    
    tm = {
        "hh": s[0],
        "mm": s[1],
        "ss": s[2]
    }
    
    if period=='AM':
        if int(tm["hh"])==12:
            tm["hh"]='00'
    elif period=='PM':
        if int(tm["hh"]) < 12:
            tm["hh"] = str(int(tm["hh"])+12)
            if len(tm["hh"]) <1:
                 tm["hh"] = '0' + tm["hh"]
    return tm["hh"] + ':' + tm["mm"] + ':' + tm["ss"]                
                 
                 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


