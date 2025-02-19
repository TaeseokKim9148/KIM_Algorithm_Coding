from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(input().strip())

max_area = 1

for i in range(N):
    for j in range(M):
        for l in range(1, min(N - i, M - j)):

            if grid[i][j] == grid[i][j + l] and grid[i][j] == grid[i + l][j] and grid[i][j] == grid[i + l][j + l]:
                area = (l + 1) * (l + 1)
                if area > max_area:
                    max_area = area

print(max_area)