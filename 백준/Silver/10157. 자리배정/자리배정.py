C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    exit()


left = 1      
right = C     
bottom = 1    
top = R       

count = 0            
result = (0, 0)       

while True:
    for y in range(bottom, top + 1):
        count += 1
        if count == K:
            result = (left, y)
            break
    if count == K:
        break
    left += 1  

    for x in range(left, right + 1):
        count += 1
        if count == K:
            result = (x, top)
            break
    if count == K:
        break
    top -= 1  

    
    for y in range(top, bottom - 1, -1):
        count += 1
        if count == K:
            result = (right, y)
            break
    if count == K:
        break
    right -= 1  

    for x in range(right, left - 1, -1):
        count += 1
        if count == K:
            result = (x, bottom)
            break
    if count == K:
        break
    bottom += 1  

print(result[0], result[1])   