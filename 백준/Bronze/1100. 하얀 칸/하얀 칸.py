Horse = []
for _ in range(8):
    Horse.append(input())

count = 0
for i in range(8):
    for j in range(8):
        if (i % 2 == j % 2) and Horse[i][j] == 'F':
            count += 1

print(count)