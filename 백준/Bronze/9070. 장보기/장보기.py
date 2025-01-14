t = int(input()) 

for _ in range(t):
    n = int(input())  #
    
    max_weight = 0 
    result = 0  
    for _ in range(n):
        w, c = map(int, input().split())  
        
        weight = w / c 
        
        
        if weight > max_weight:
            max_weight = weight
            result = c
        
        elif weight == max_weight and c < result:
            result = c
    
    
    print(result)