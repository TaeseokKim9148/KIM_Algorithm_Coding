import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s = input().strip()
    x, y, d = 0, 0, 0
    min_x = max_x = 0
    min_y = max_y = 0
    for c in s:
        if c == 'F':
            if d == 0: y += 1
            elif d == 1: x += 1
            elif d == 2: y -= 1
            elif d == 3: x -= 1
        elif c == 'B':
            if d == 0: y -= 1
            elif d == 1: x -= 1
            elif d == 2: y += 1
            elif d == 3: x += 1
        elif c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y
    print((max_x - min_x) * (max_y - min_y))