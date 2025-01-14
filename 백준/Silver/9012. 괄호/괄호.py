T = int(input())  

for _ in range(T):
    stack = []    
    i = input()   
    is_vps = True 
    
    for v in i:
        if v == '(':     
            stack.append(v)   
        else:           
            if stack:    
                stack.pop()  
            else:        
                is_vps = False  
                break
    if stack:       
        is_vps = False  
    
    print('YES' if is_vps else 'NO')