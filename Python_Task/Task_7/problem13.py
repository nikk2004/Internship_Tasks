# 13. Sherlock and the Valid String
# Hackerrank Link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    from collections import Counter

    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) == 2:
        f1, f2 = freq_count.keys()

        if freq_count[f1] == 1 and (f1 - 1 == f2 or f1 == 1):
            return "YES"

        if freq_count[f2] == 1 and (f2 - 1 == f1 or f2 == 1):
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
