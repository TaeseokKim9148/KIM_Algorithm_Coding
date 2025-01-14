import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = sorted([int(input()) for _ in range(M)], reverse= True)

max_revenue = 0
best_price = 0

for i in range(M):
    price = P[i]
    count = min(i + 1 , N)
    revenue = price * count
            
    if revenue > max_revenue:
        max_revenue = revenue
        best_price = price

print(best_price, max_revenue)