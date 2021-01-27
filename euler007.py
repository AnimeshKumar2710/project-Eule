import sys

def isprime(num):
    for i in range (2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    count = 0
    while 1:
        if isprime(i):
            count+= 1
            if count == n:
                print(i)
                break
        i += 1
