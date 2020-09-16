# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:03:46 2020

@author: Yuling Gu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    round_grade = []
    for grade in grades:
        last = grade%10
        if grade < 38:
            round_grade.append(grade)
        else:
            if last > 5:
                check = 10 - last
                if check < 3:
                    round_grade.append(round(grade,-1))
                else:
                    round_grade.append(grade)
            else:
                check = 5 - last
                if check < 3:
                    round_grade.append(grade+check)
                else:
                    round_grade.append(grade)
    return round_grade


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
