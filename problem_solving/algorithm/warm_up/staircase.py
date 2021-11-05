# Its base and height are both equal to . It is drawn using # symbols and spaces. 
# The last line is not preceded by any spaces.
# Write a program that prints a staircase of size .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):                   # i = 3
    for i in range(n):               # j = 0 --> sss
        for j in range(n-i-1):        # k = 4 --> #
            print(' ', sep='', end='')
        for k in range(i+1):
            print('#', sep='', end='')
        print('', end='\n')
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
