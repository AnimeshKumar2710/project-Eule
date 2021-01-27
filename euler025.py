limit = 5001
indexs = [1 for i in range(limit)]
check = 9
k = 1
first = 1
second = 1
index = 2
indexs[0] = 0
while k < limit:
    fib = first + second
    second = first 
    first = fib
    index += 1
    if fib > check:
        check = check * 10 + 9
        
        indexs[k] = index
        k += 1
        
t = int(input())
for a in range (t):
    n = int(input())
    print(indexs[n - 1])
    
