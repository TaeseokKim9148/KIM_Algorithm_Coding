N, M = map(int, input().split()) 
numbers = list(map(int, input().split()))  
numbers.sort()  

result = []  
used = [False] * N  

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    last_used = -1
    
    for i in range(N):
        if used[i] or numbers[i] == last_used:
            continue
            
        used[i] = True
        result.append(numbers[i])
        last_used = numbers[i]  
        
        backtrack()
        
        result.pop()
        used[i] = False

backtrack()  