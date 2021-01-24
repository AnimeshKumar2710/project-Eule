#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n < 1:
        print(0)
    else:
        a = int((n - 1) / 3)
        b = int((n - 1) / 5)
        c = int((n - 1) / 15)
        a = 3 * int((a * (a + 1)) >> 2)
        b = 5 * int((b * (b + 1)) >> 2)
        c = 15 * int((c * (c + 1)) >> 2)
        print(a + b - c)
