n, q = map(int, input().split())


slots = [1] * (n + 1)  


for _ in range(q):
    l, i = map(int, input().split())
    
    for pos in range(l, n + 1, i):
        slots[pos] = 0  
             

print(sum(slots) -1)