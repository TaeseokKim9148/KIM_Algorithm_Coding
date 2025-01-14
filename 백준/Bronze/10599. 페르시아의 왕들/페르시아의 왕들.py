while True:

    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    min_a = c - b
    max_a = d - a
    print(min_a, max_a)