def pinary_number(n):

    dp = [[0, 0] for _ in range(n + 1)]
    
    # 초기값 설정
    if n >= 1:
        dp[1][0] = 0  
        dp[1][1] = 1 
    
    #DP 계산 
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        
        dp[i][1] = dp[i-1][0]
    
    return dp[n][0] + dp[n][1]

n = int(input())

result = pinary_number(n)
print(result)