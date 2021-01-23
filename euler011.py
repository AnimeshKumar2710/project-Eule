import sys


grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    for i in range(4):
        grid_temp.insert(0, 0)
        grid_temp.append(0)
    grid.append(grid_temp)
zeros = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (4):
    grid.insert(0, zeros)
    grid.append(zeros)
top = 0
for i in range(3, 24, 1):
    for j in range (3, 24, 1):
        mul = [1, 1, 1, 1]
        for k in range (4):
            mul[0] *= grid[i - k][j + k]
            mul[1] *= grid[i + k][j]
            mul[2] *= grid[i][j + k]
            mul[3] *= grid[i + k][j + k]
        if top < max(mul):
            top = max(mul)
print(top)
