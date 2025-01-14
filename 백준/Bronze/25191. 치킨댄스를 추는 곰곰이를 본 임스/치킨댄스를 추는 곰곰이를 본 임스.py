n = int(input())

a, b = map(int, input().split())

e = a//2 + b

if n >= e:
    print(e)
else:
    print(n)