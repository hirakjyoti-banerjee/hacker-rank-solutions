#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c,n):
    # Write your code here
    cnt = 0
    i=0
    while i < n-2:
        if c[i+2] == 0:
            i=i+2
        else:
            i=i+1
        cnt +=1
    
    if i != n-1:
        cnt +=1
        
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    fptr.write(str(result) + '\n')

    fptr.close()
