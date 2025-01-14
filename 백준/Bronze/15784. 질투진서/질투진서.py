n, a, b = map(int, input().split())

x = [list(map(int, input().split())) for _ in range(n)]

jin = x[a-1][b-1]

c = False

for j in range(n):
    if x[a-1][j] > jin or x[j][b-1] > jin:
        c = True
        break

if c: 
    print("ANGRY")
else:
    print("HAPPY")