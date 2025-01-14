P = int(input())  

for _ in range(P):
    
    numbers = list(map(int, input().split()))
    T = numbers[0]      
    heights = numbers[1:]  
    
    line = []  
    total_steps = 0  
    
    
    for height in heights:
        
        if not line or height > line[-1]:
            line.append(height)
            continue
            
        
        for i in range(len(line)):
            if height <= line[i]:
                line.insert(i, height)  
                total_steps += len(line) - i - 1  
                break
    
    print(T, total_steps)