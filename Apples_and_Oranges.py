# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:13:27 2020

@author: betty
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    s: integer, starting point of Sam's house location.
    t: integer, ending location of Sam's house location.
    a: integer, location of the Apple tree.
    b: integer, location of the Orange tree.
    apples: integer array, distances at which each apple falls from the tree.
    oranges: integer array, distances at which each orange falls from the tree.
    """
    apples_new = [a + apple for apple in apples]
    oranges_new =[b + orange for orange in oranges]

    apples_in = [i for i in apples_new if (i >= s) & (i <= t)]
    oranges_in = [i for i in oranges_new if(i >= s) & (i <= t)]

    print(len(apples_in))
    print(len(oranges_in))

    #return len(apples_in), len(oranges_in)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
