#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    level = 0
    for i in range(steps):
        if level == 0 and path[i] == 'D':
            valley += 1
        if path[i] == 'U':
            level += 1
        else:
            level -= 1
    return valley
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input().strip()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
