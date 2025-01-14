N, M, K = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

lengths = [0] * N
person_counts = [0] * N

for j in range(M):
    for i in range(N):
        lengths[i] += A[i][j]
        person_counts[i] += 1
        
        if lengths[i] >= K:
            print(i + 1, person_counts[i])
            break
    else:
        continue
    break