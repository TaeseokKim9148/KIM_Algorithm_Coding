n, m = map(int, input().split())

ml = {}
for i in range(1, m+1):
    ml[i] = {}  


arr = []
for i in range(n):
    p, w = map(int, input().split())
    
    if w not in ml[p]:
        ml[p][w] = 0
    ml[p][w] += 1
    arr.append((p, w))

now = m
ans = 0  
s = [0]  

while arr:
    prior, front = arr[0]  
    arr = arr[1:]  
    
    while now != prior:
        ans += front  
        arr.append((prior, front))  
        prior, front = arr[0]  
        arr = arr[1:]  
    
    ml[now][front] -= 1
    if ml[now][front] == 0:
        del ml[now][front]  
    
    if s:
        lift = []  
        
        while s and s[0] < front:
            top = s[0]  
            s = s[1:]  
            lift.append(top)  
            ans += top  
        
        s.insert(0, front)
        
        while lift:
            top = lift.pop()  
            ans += top  
            s.insert(0, top)  
        
        ans += front  
    
    if len(ml[now]) == 0:
        s = [0]  
        now -= 1  

print(ans)