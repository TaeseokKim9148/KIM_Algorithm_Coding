import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())

photo = []
for _ in range(R):
    photo.append(list(map(int, input().split())))

sum_table = [[0] * (C + 1) for _ in range(R + 1)]

for i in range(1, R + 1):
    for j in range(1, C + 1):
        sum_table[i][j] = (
            sum_table[i-1][j] + sum_table[i][j-1] 
            - sum_table[i-1][j-1] + photo[i-1][j-1]
        )

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    total = (
        sum_table[r2][c2]
        - sum_table[r1-1][c2]
        - sum_table[r2][c1-1]
        + sum_table[r1-1][c1-1]
    )
    count = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(total // count)