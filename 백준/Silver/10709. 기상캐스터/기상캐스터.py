H, W = map(int, input().split())

sky = []
for _ in range(H):
    sky.append(input())

for i in range(H):
    answer = [] 
    
    for j in range(W):
        if sky[i][j] == 'c':  
            answer.append(0)  
        else:  
            min_time = -1  

            for k in range(j):
                if sky[i][k] == 'c':
                    time = j - k  
                    if min_time == -1 or time < min_time:
                        min_time = time
            
            answer.append(min_time)
    
    print(*answer)