n, w, h = map(int,input().split())

a = (w**2 + h**2)**0.5 # 수학적인 표현이라서 찾아봄

for _ in range(n):
    b = int(input())
    if b <= a:
        print('DA')
    else:
        print('NE')