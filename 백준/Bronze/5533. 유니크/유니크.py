N = int(input())


numbers = [list(map(int, input().split())) for _ in range(N)]


scores = [0] * N


for game in range(3):
    count = {}  

    
    for player in range(N):
        num = numbers[player][game]
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

   
    for player in range(N):
        num = numbers[player][game]
        if count[num] == 1:  
            scores[player] += num  


print(*scores)