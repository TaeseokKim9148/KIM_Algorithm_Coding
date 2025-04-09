def stone(n):
    dp = [0] * (n + 1)
    
    dp[0] = 0 
    dp[1] = 1 
    
    for i in range(2, n+1):
        if i >= 1 and dp[i-1] == 0:
            dp[i] = 1 
        elif i >= 3 and dp[i-3] == 0:
            dp[i] = 1 
        elif i >= 4 and dp[i-4] == 0:
            dp[i] = 1 
        else:
            dp[i] = 0 
    
    return dp[n]


n = int(input())



winner = stone(n)
if winner == 1:
    print("SK")  
else:
    print("CY") 