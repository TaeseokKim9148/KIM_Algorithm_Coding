W = 0
W_s = 0

for i in range(1, 6):
    s = list(map(int, input().split()))
    t = sum(s)
    
    if W_s < t:
        W_s = t
        W = i

print(W, W_s)
        
