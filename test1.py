#!/bin/python3

import math
import os
import random
import re
import sys


def multiply(a, b, bound):

    if a * b > bound:
        raise ValueError(f"multiplication of {a} and {b} with bound {bound} not possible")
    else:
        return a*b

if __name__ == '__main__':

    q = int(input())
    for _ in range(q):
        a, b, bound = list(map(int, input().split()))
        try:
            res = multiply(a, b, bound)
            print(res)
        except ValueError as e:
            pass
