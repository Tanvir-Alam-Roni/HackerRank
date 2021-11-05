# Problem:
#         You are asked to ensure that the first and
#         last names of people begin with a capital letter in their passports. 
#         For example, alison heck should be capitalised correctly as Alison Heck.
#         Given a full name, your task is to capitalize the name appropriately.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    name_list = s.split(' ')
    name_cap = [name.capitalize() for name in name_list]
    return ' '.join(name_cap)
# solution 1 >> runtime error
# def solve(s):
#     cap_name = []
#     names = s.split(' ')
#     for name in names:
#         name = re.sub(name[0], name[0].upper(), name)
#         cap_name.append(name)
#     return ' '.join(cap_name)

        
    return lists   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
