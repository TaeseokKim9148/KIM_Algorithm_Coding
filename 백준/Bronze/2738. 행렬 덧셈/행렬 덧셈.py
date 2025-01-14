a, b = [], []
n, m = map(int,input().split())

for i in range(n):
    r = list(map(int,input().split()))
    a.append(r)

for i in range(n):
    r = list(map(int,input().split()))
    b.append(r)
# 행렬 a, b 에 저장되어 있는 값을 각각 더한 행렬의 값을 출력
for r in range(n):
    for c in range(m):
        print(a[r][c] + b[r][c], end=' ')
    print()