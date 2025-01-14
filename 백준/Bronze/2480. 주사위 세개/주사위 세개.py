A, B, C = map(int,input().split())

if A == B == C:  
    p = 10000 + A * 1000
elif A == B or A == C:
    p =  1000 + A * 100
elif B == C:
    p = 1000 + B * 100
else:
    p= max(A, B, C) * 100

print(p)