t = int(input())

for _ in range(t) :
    n, k = map(int,input().split())
    c = list(map(int, input().split()))
    a = 0
    for i in c :
        a += i // k
    print(a) 



