import sys
input = sys.stdin.readline  


N, M = map(int, input().split())  


sum_table = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        # 현재 위치까지의 누적 합 계산
        sum_table[i][j] = sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1] + row[j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    

    result = sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]
    
    print(result)