temp = 1000000007
def fect(num):
    if num == 1:
        return 1
    else:
        return num * fect(num - 1)
    
t= int(input())
for i in range (t):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    nm = fect(n + m)
    n = fect(n)
    m = fect(m)
    print(int((nm // (n * m)) % (temp)))
