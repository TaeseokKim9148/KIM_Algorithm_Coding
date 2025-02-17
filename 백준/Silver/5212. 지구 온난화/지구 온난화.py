import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
for _ in range(R):
    line = input().strip()
    grid.append(list(line))

future_grid = []
for i in range(R):
    future_grid.append(grid[i][:])

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'X':
            sea_count = 0

            if i - 1 < 0:
                sea_count += 1
            else:
                if grid[i-1][j] == '.':
                    sea_count += 1

            if i + 1 >= R:
                sea_count += 1
            else:
                if grid[i+1][j] == '.':
                    sea_count += 1

            if j - 1 < 0:
                sea_count += 1
            else:
                if grid[i][j-1] == '.':
                    sea_count += 1

            if j + 1 >= C:
                sea_count += 1
            else:
                if grid[i][j+1] == '.':
                    sea_count += 1

            if sea_count >= 3:
                future_grid[i][j] = '.'

min_i = R
max_i = -1
min_j = C
max_j = -1

for i in range(R):
    for j in range(C):
        if future_grid[i][j] == 'X':
            if i < min_i:
                min_i = i
            if i > max_i:
                max_i = i
            if j < min_j:
                min_j = j
            if j > max_j:
                max_j = j

for i in range(min_i, max_i + 1):
    row = future_grid[i][min_j:max_j + 1]
    print(''.join(row))