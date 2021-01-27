arr = 'abcdefghijklm'

def findfact(n):
    i = 1
    fact = [0 for i in range(13)]
    while n:
        fact[13 - i] = n % i
        n = n // i
        i += 1
    return fact

def findstr(n):
    result = ''
    listarr = list(arr)
    for i in range(len(n)):
        result += listarr.pop(n[i])
    return result 

t = int(input())

for a in range(t):
    n = int(input())
    fact = [0] * 13
    fact = findfact(n - 1)
    arr2 = findstr(fact)
    print(arr2)
