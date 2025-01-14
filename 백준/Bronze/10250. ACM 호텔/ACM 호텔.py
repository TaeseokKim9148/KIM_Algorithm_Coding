t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    f = n % h
    l = (n //h) +1 
    if f == 0:
        f = h 
        l  -= 1

    a = f * 100 + l

    print(a)