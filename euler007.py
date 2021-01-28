limit = 104801
import sys
import math
prime = []
prime.append(1)
prime.append(2)
def isprime(num):
    check = 1
    for i in range(1, len(prime)):
        if num % prime[i] == 0:
            check = 0
            break
        elif prime[i] > num //2:
            break
    if check == 1:
        prime.append(num)

for i in range (3,limit):
    isprime(i)
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime[n])
