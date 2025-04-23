import sys
input = sys.stdin.readline

n = int(input())  
wines = [0] 

for i in range(n):
    wines.append(int(input()))

dp = [0] * (n + 1)

# 기본 값 설정
if n >= 1:
    dp[1] = wines[1]
if n >= 2:
    dp[2] = wines[1] + wines[2]

for i in range(3, n + 1):

    dp[i] = max(
        dp[i-1],  # i번째 안 마심
        dp[i-2] + wines[i],  # i번째 마시고, i-1번째 안 마심
        dp[i-3] + wines[i-1] + wines[i]  # i, i-1번째 마시고, i-2번째 안 마심
    )
print(dp[n])