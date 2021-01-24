import sys
sys.setrecursionlimit(15000)
def pow2(num):
    if num == 1:
        return 2
    else:
        return 2 * pow2(num - 1)
  
t = int(input())
for i in range(t):
    n = int(input())
    p = pow2(n)
    sumdig = 0
    for i in str(p):
        sumdig += int(i)
    print(sumdig)
