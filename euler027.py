limit = 50000
primes = []

def isprime(num):
    for i in range (2, int(num / 2)):
        if num % i == 0:
            return False
    return True

for i in range ( limit):
    if isprime(i):
        primes.append(i)

n = int(input())

for i in range (limit):
    if primes[i] >= n:
        index = i - 1
        break

b = primes[index]

count = 0
if n % 2 == 0:
    n -= 1

a = 0
for j in range(index, -1, -1):
    b1 = primes[j]
    for i in range (-n, n + 1, 2):
        temp = 0
        for k in range(0, n):
            if ((k * k) + (i * k) + b1) not in primes:
                break 
            else:
                temp += 1
        if count < temp:
            count = temp
            a = i 
            b = b1
        
