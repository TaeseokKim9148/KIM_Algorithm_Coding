import sys
input = sys.stdin.readline

n = int(input())

costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

# dp 테이블 초기화
# dp[i][j]는 i번째 집을 j색으로 칠했을 때의 최소 비용
# j=0은 빨강, j=1은 초록, j=2는 파랑
dp = [[0, 0, 0] for _ in range(n)]

dp[0][0] = costs[0][0]  
dp[0][1] = costs[0][1]  
dp[0][2] = costs[0][2]  

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

min_cost = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(min_cost)