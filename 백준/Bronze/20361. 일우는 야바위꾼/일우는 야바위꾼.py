n, x, k = map(int,input().split())
p = x

for _ in range(k): 
    a, b = map(int,input().split())
    
    if p == a:
        p = b
    elif p == b:
        p = a
        
print(p)