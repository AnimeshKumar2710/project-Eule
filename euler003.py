import sys

def isprime(num):
    for i in range (2, int(num / 2)):
        if num % i == 0:
            return False
    return True
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if isprime(n):
        print(n)
    else:
        for i in range (int(n / 2) + 1, 2, -1):
            if n % i == 0 and isprime(i):
                    print(i)
                    break
