
import math
limit = 100001
factors = [-i for i in range(limit)]
def findfactors(num):
    for k in range  (1, int(math.sqrt(num)) + 1):
        if num % k == 0:
            if num / k == k :
                factors[num] += int(k)
            else:
                factors[num] += int(k) + int(num / k) 
                

for i in range(1, limit):
    findfactors(i)
    


t = int(input())
for a in range (t):
    n = int(input())
    sums = 0
    if n < limit:
        for i in range ( 2, n + 1):
            if factors[i] < limit:
                if factors[factors[i]] == i and factors[i] != i:
                    sums += i
            else:
                temp = findfactors(factors[i])
                if temp ==  i:
                    sums += i
    else:
        
        factors2 = [findfactors(i) - i for i in range(limit, n)]
        for i in range ( 2, limit):
            if factors[i] < limit:
                if factors[factors[i]] == i and factors[i] != i:
                    sums += i
            else:
                temp = findfactors(factors[i])
                if temp ==  i:
                    sums += i
        for i in range(limit, n + 1):
            if factors[i] < n:
                if factors[factors[i]] == i and factors[i] != i:
                    sums += i
            else:
                temp = findfactors(factors[i])
                if temp ==  i:
                    sums += i
            
                            
    print(sums)
