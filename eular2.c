import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
   
    pre = 1;
    curr = 1;
    sum = 0;
    while curr < n:
            
        if curr % 2 == 0:
            sum += curr
            
        temp = curr
        curr += pre
        pre = temp
            
    print(sum)
