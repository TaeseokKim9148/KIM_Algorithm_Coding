import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = []
for _ in range(N):
    row = list(map(int, input().split()))
    basket.append(row)

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

diag_dx = [-1, -1, 1, 1]
diag_dy = [-1, 1, 1, -1]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        moved_clouds.append((nx, ny))
    
    water_increased = set()
    
    for x, y in moved_clouds:
        basket[x][y] += 1
        water_increased.add((x, y))
    
    
    for x, y in moved_clouds:
        count = 0
        for i in range(4):
            nx = x + diag_dx[i]
            ny = y + diag_dy[i]
            if 0 <= nx < N and 0 <= ny < N and basket[nx][ny] > 0:
                count += 1
        basket[x][y] += count
    
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and (i, j) not in water_increased:
                basket[i][j] -= 2
                new_clouds.append((i, j))
    
    clouds = new_clouds

total_water = 0
for i in range(N):
    for j in range(N):
        total_water += basket[i][j]

print(total_water) 