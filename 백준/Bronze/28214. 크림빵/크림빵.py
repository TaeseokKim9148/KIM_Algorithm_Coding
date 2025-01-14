N, K, P = map(int, input().split())
bread = list(map(int, input().split()))


pal = 0

for i in range(N):
    start = i * K
    end = start + K
    mug = bread[start:end]
    
   
    if mug.count(0) < P:
        pal += 1


print(pal)