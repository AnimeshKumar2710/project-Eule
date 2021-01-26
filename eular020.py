limit = 1000
fact = [1 for i in range (limit + 1)]

for i in range (1, limit + 1):
    fact[i] = i * fact[i - 1]


def counts(num):
    sumdig = 0
    while num :
        temp = num % 10
        num = num // 10
        sumdig += temp
    return sumdig
        
        
t = int(input())
for a in range(t):
    n = int(input())
    print (counts(fact[n]))
