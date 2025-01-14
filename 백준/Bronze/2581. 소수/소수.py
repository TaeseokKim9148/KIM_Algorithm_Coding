m = int(input())
n = int(input())

sosu = []

for i in range(m, n+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j ==0:
                count += 1
                break
        if count == 0:
            sosu.append(i)
    
if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)