n, m = map(int, input().split())

b = [] # 붕어빵을 담을 틀

for _ in range(n):
    c = list(input()) # 붕어빵을 틀에 넣어주는 과정
    b.append(c)

for c in b: 
    for i in range(len(c) -1, -1, -1):
        print(c[i], end = '')

    print()