limit = 1000001
prime =[True for i in range (limit)]

p = 2
while p * p < limit:
    
    if prime[p] == True:
        
         for i in range (p * p,limit, p):
            prime[i] = False
    p += 1
sums = [0 for i in range(limit)]
for i in range (1, limit):
    sums[i] += sums[i -1]
    if prime[i]:
        sums[i] += i
t = int(input())
for a in range (t):
    n = int(input())
    print(sums[n] - 1)
