N = int(input())
room = []

for _ in range(N):
    row = input()
    room.append(row)

width = 0
for i in range(N):
    count = 0
    for j in range(N):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                width += 1
            count = 0
    if count >= 2:
        width += 1

height = 0
for j in range(N):
    count = 0
    for i in range(N):
        if room[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                height += 1
            count = 0
    if count >= 2:
        height += 1

print(width, height)  