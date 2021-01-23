t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    cyc = 1
    add = 1
    while 1:
        add += i
        i += 1
        count = 1
        for k in range (2, int(add / 2) + 1):
            if add % k == 0:
                count+= 1
        if count >= n:
            print(int(add))
            break
