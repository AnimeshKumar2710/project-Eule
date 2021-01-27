import sys
palin = []

for i in range (100, 1000):
    for j in range (100, 1000):
        mul = i * j
        
        if str(mul) == str(mul)[::-1] and mul not in palin:
            palin.append(mul)
palin.sort()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    for i in range (len(palin) - 1, -1, -1):
        if palin[i] < n:
            print (palin[i])
            break
