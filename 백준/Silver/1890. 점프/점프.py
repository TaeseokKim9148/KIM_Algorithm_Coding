import sys
input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dp[N-1][N-1] = 1

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if i == N-1 and j == N-1:
            continue
            
        jump = board[i][j]
        
        if jump == 0:
            continue
            
        if j + jump < N:
            dp[i][j] += dp[i][j + jump]
            
        if i + jump < N:
            dp[i][j] += dp[i + jump][j]
            
print(dp[0][0])