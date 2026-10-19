# Q3. Mars Exploration

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'marsExploration' function below.
# Hackerrank Link : https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(s):
    count = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            count += 1

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
