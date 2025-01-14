n= int(input())

c = list(map(int, input().split()))

a = b= 0

for i in c:
    a += (i//30 + 1) * 10
    b += (i//60 + 1) * 15

if a < b:
    print('Y', a)
elif a == b:
    print('Y M', a)
else:
    print('M', b)