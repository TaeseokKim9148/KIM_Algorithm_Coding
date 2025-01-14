h = [int(input()) for _ in range(9)]  
t = sum(h)  #

for i in range(9):
    for j in range(i + 1, 9):
        if t - h[i] - h[j] == 100:
            f1, f2 = h[i], h[j]
            break

for height in h:
    if height not in [f1, f2]:
        print(height)
