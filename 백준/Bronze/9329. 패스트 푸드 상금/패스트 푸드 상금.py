T = int(input())  

for _ in range(T):
    n, m = map(int, input().split())
    
    sticker_need = []   
    prize_money = []     
    
    for _ in range(n):
        info = list(map(int, input().split()))
        k = info[0]                 
        need = info[1:k+1]          
        money = info[-1]           
        sticker_need.append(need)   
        prize_money.append(money)   

    have = list(map(int, input().split()))

    total = 0
    for i in range(n):
        min_count = 100
        for sticker in sticker_need[i]:
            count = have[sticker-1]
            if count < min_count:
                min_count = count
        
        total += min_count * prize_money[i]
    
    print(total)