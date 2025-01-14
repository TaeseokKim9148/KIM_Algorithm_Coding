C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    exit()

dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]  

x, y = 1, 0  
direction = 0  
count = 0  

seats = [[0] * (R + 1) for _ in range(C + 1)]


while count < K:

    next_x = x + dx[direction]
    next_y = y + dy[direction]
    

    if (1 <= next_x <= C and 1 <= next_y <= R and seats[next_x][next_y] == 0):
        x, y = next_x, next_y  
        count += 1  
        seats[x][y] = count  
    else:
        direction = (direction + 1) % 4 

print(x, y)