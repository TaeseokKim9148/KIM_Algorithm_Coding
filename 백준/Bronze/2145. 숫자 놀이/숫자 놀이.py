while True:
    n = input().strip()  
    if n == "0": 
        break
    
    while len(n) > 1:  
        total = 0
        for i in n:
            total += int(i)  
        n = str(total)  # 문자열로 변환
    
    print(n)  