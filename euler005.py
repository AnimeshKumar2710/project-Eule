import sys

def isprime(num):
    for i in range (2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    mul = 1
    for k in range(2, n + 1):
        if isprime(k):
            temp = k
            while temp * k <= n:
                temp *= k
            mul *= temp  
    
    print(mul)
