t = int(input())
for a in range (t):
    n = int (input())
    arr =[]
    graph = {}
    value = {}
    for i in range(n):
        temp = [int(x) for x in input().split()]
        arr.append(temp)
    i = n - 2
    while i >= 0:
        for k in range(len(arr[i])):   
            arr[i][k] += max(arr[i + 1][k], arr[i + 1][k + 1])
        i -= 1
    print(arr[0][0])
