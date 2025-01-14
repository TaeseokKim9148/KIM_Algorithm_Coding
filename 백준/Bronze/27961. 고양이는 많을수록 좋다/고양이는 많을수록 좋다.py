N = int(input())

if N == 0:
    print(0)
else:
    count = 1  
    cats = 1   
    
    while cats < N:
        
        can_clone = cats
        
        need_cats = N - cats
        
        if need_cats <= can_clone:
            cats = cats + need_cats 
            count += 1
            break
        else:
            cats += can_clone
            count += 1
            
    print(count)