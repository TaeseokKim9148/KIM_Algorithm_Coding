import sys
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

apples = set()
for _ in range(K):
    row, col = map(int, input().strip().split())
    apples.add((row, col))  # 사과 위치를 튜플로 저장

L = int(input().strip())
direction_changes = {}
for _ in range(L):
    X, C = input().strip().split()
    direction_changes[int(X)] = C  

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
direction = 0
snake = [(1, 1)]

while True:
    time += 1
    
    head_x, head_y = snake[0]
    
    next_x = head_x + dx[direction]
    next_y = head_y + dy[direction]
    
    if next_x < 1 or next_x > N or next_y < 1 or next_y > N or (next_x, next_y) in snake:
        break
    
    snake.insert(0, (next_x, next_y))
    
    if (next_x, next_y) in apples:
        apples.remove((next_x, next_y))
    else:
        snake.pop()
    
    if time in direction_changes:
        if direction_changes[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)