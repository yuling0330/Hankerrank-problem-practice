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


def countingValleys(n, s):
    res=0
    vally =0
    for i in range(0,n):
        if s[i] == "U":
            res += 1
            if res== 0:
                vally +=1
        if s[i] == "D":
            res -= 1

        #print(res)
    return vally