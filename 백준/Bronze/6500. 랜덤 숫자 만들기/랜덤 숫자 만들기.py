while True:
    a0 = input().strip()  
    if a0 == '0':  
        break

    seen = set()  
    current = int(a0)  

    while current not in seen:  
        seen.add(current)  
        squared = str(current ** 2) 

        
        if len(squared) < 8:
            squared = '0' * (8 - len(squared)) + squared

        current = int(squared[2:6])  

    print(len(seen)) 