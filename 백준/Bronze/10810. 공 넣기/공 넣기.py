N, M = map(int, input().split())
    
b = [0] * N
    
for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i -1, j):
        b[index] = k

for i in range(N):
    print(b[i], end= ' ')








