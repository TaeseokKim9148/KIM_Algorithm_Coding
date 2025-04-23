import sys
input = sys.stdin.readline

N = int(input())

T = []
P = []

for _ in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N):
    if i  + T[i] <=N:
        dp[i + T[i]] = max(dp[i + T[i]],dp[i] + P[i])

    if i + 1 <= N :
        dp[i + 1] = max(dp[i + 1],dp[i])

print(dp[N])