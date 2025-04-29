import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))

prefix_sum = [0] * N
prefix_sum[0] = A[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + A[i]

values = [(prefix_sum[i], i) for i in range(N)]
values.sort(reverse=True)

destinations = [values[i][1] for i in range(K)]

visit_change = [0] * (N + 1)

for dest in destinations:
    visit_change[0] += 1
    visit_change[dest + 1] -= 1

visits = [0] * N
current = 0
for i in range(N):
    current += visit_change[i]
    visits[i] = current

total_score = sum(A[i] * visits[i] for i in range(N))

print(total_score)