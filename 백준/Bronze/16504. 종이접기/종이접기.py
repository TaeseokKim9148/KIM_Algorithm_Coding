n = int(input())

total = 0

for _ in range(n):
    total += sum(map(int,input().split()))

print(total)