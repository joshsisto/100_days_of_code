#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def diagonalDifference(arr):
    a = arr
    if len(a) == 4:
        fdiag = a[0][0] + a[1][1] + a[2][2]
        sdiag = a[0][2] + a[1][1] + a[2][0]
        answer = fdiag - sdiag
        return abs(answer)
    if len(a) == 5:
        fdiag = a[0][0] + a[1][1] + a[2][2] + a[3][3]
        sdiag = a[0][3] + a[1][2] + a[2][1] + a[3][0]
        answer = fdiag - sdiag
        return abs(answer)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = [4, 5, 6]

    b = [5, 6, 5]

    array1 = [[4],
           [-1, 1, -7, -8],
           [-10, -8, -5, -2],
           [0, 9, 7, -1],
           [4, 4, -2, 1]]



    result = diagonalDifference(array1)
    result2 = diagonalDifference(array1)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
    # print(result)
