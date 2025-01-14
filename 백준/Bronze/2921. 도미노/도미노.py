n = int(input())
t = 0
for i in range(n+1):
    for j in range(i, n+1):
        t += (i+j)
print(t)
