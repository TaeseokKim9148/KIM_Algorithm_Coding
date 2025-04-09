def stairs(n, stairs):

    if n == 1:
        return stairs[0]
    if n == 2:
        return stairs[0] + stairs[1]

    dp = [0] * n

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    return dp[n - 1]


n = int(input())

stairs1 = []
for _ in range(n):
    stairs1.append(int(input()))

result = stairs(n, stairs1)
print(result)