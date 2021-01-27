import math

def findtrue(num):
    sumval = -1 * num
    for k in range  (1, int(math.sqrt(num)) + 1):
        
        if num % k == 0:
            if num / k == k :
                sumval += int(k)
            else:
                sumval += int(k) + int(num / k) 
        if sumval > num:
            return 'YES'
    
    return 'NO'


t= int(input())

for a in range(t):
    n = int(input())
    print(findtrue(n))
