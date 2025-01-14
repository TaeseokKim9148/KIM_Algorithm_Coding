n, m = map(int, input().split())  
senong = [input().strip() for _ in range(n)]  

row_count = 0
for i in range(n):
    if 'X' not in senong[i]:  
        row_count += 1


col_count = 0
for j in range(m):
    find = False
    for i in range(n):
        if senong[i][j] == 'X':  
            find = True
            break
    if not find:  
        col_count += 1

print(max(row_count, col_count))