case = 1  

while True:
    L, P, V = map(int, input().split())
    
    if L == 0:  
        break
        

    camping = (V//P) * L
    
    if (V%P) > L:  
        camping += L  
    else:  
        camping += (V%P)  
        
    print(f"Case {case}: {camping}")
    case += 1