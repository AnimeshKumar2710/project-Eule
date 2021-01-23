import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = -1
    for a in range (2, int(n / 3)):
         b = (n * n - 2 * n * a)/(2 * n - 2 * a);
         if b - int(b) == 0:
             c = n - a - b;
             if (a * a) + ( b * b) == (c * c):
                temp = a * b * c
                if ans < temp and temp > 0:
                    ans = math.trunc(temp)
                
    print(ans)
