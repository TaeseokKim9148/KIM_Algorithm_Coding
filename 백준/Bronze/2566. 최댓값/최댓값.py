t = [list(map(int, input().split())) for _ in range(9)]
max_n = 0
max_r,max_c = 0, 0
for r in range(9):
    for c in range(9):
        if max_n <= t[r][c]:
            max_r = r
            max_c = c
            max_n = t[r][c]
print(max_n)
#1부터 시작하는 인덱스(1-based indexing)
print(max_r+1,max_c+1)