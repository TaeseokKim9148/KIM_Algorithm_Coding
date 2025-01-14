a , b = map(int,input().split())
# 방어률
e = a - (a *  b / 100)

if e >= 100:
    print(0)
else: 
    print(1)