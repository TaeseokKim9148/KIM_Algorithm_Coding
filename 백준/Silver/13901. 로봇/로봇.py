R, C = map(int, input().split())

k = int(input())

block = set()
for _ in range(k):
    br, bc = map(int, input().split())
    block.add((br, bc))

sr, sc = map(int, input().split())
directions = list(map(int, input().split()))

move = {
    1: (-1, 0),  # 위
    2: (1, 0),   # 아래
    3: (0, -1),  # 왼쪽
    4: (0, 1)    # 오른쪽
}

visited = set()
visited.add((sr, sc))

current_r, current_c = sr, sc

direction_index = 0
consecutive_failures = 0

while True:
    dr, dc = move[directions[direction_index]]
    next_r = current_r + dr
    next_c = current_c + dc
    
    # 이동 가능한지 검사
    if (0 <= next_r < R and 0 <= next_c < C and 
        (next_r, next_c) not in block and 
        (next_r, next_c) not in visited):
        
        # 이동 성공
        current_r, current_c = next_r, next_c
        visited.add((current_r, current_c))
        consecutive_failures = 0 
        
    else:
        consecutive_failures += 1
        direction_index = (direction_index + 1) % len(directions)
        
        if consecutive_failures >= len(directions):
            break
    
print(current_r, current_c)