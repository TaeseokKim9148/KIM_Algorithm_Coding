import sys
input = sys.stdin.readline  

n = int(input())
numbers = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

m = int(input())

results = []

for _ in range(m):
    i, j = map(int, input().split())
    results.append(prefix_sum[j] - prefix_sum[i-1])

for result in results:
    print(result)