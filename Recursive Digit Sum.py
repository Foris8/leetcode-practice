#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    def solve(n):
        if len(n) == 1:
            return n[0]
        sum = 0
        for digit in n:
            sum += int(digit)
        return solve(list(str(sum)))

    sum = 0
    for digit in n:
        sum += int(digit)
    sum *= k

    result = solve(list(str(sum)))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
