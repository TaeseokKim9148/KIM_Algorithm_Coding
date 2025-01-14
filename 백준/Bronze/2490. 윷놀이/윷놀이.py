for _ in range(3):
    a = list(map(int, input().split()))
    b = sum(a)
    c = ['D', 'C', 'B', 'A', 'E']

    print(c[b])