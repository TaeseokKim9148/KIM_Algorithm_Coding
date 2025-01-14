t = int(input())  

for _ in range(t):
    input()  
    n = int(input())  
    c = 0  
    for _ in range(n):
        c += int(input())  
    if c % n == 0:  
        print('YES')  
    else: 
        print('NO')  