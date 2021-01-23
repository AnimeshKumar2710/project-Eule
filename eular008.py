from operator import mul
import sys
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    arr = []
    top = 0
    arr= [int(a) for a in str(num)]
    prod = []

    for h in range (len(arr) - k):
        prod.append(reduce(mul, arr[h: h+k]))
            
    print(max(prod))
