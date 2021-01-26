names = {}
name = []
def findval(arr):
    val = 0
    for i in range(len(arr)):
        if ord(arr[i]) > 96 and ord(arr[i]) < 123:
            val += (ord(arr[i]) - 96)
        if ord(arr[i]) > 64 and ord(arr[i]) < 91:
            val += (ord(arr[i]) - 64)
    return val
    
t = int(input())

for a in range(t):
    name.append(input())
name.sort()


for i in range (len(name)):
    names[name[i]] = (i + 1) * findval(name[i])

n = int(input())

for i in range(n):
    check = input()
    print(names[check])
