#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxBeauty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaxBeauty(arr):

    psum = generate_psum(arr)


def generate_psum(arr):

    psum = []
    temp = 0
    for num in arr:
        temp = temp + num
        psum.append(temp)

    return psum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMaxBeauty(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
