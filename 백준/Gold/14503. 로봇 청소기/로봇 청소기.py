import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]


count = 0

while True:

    if room[r][c] == 0:
        room[r][c] = 2  
        count += 1
    
    cleaned = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            cleaned = False
            break
    
    if cleaned:
        back_d = (d + 2) % 4
        nr = r + dr[back_d]
        nc = c + dc[back_d]
        
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
            r, c = nr, nc
        else:
            break
    
    else:
        d = (d - 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc

print(count)