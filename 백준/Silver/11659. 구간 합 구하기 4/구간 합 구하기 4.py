import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

sum_list = [0]

total = 0

for i in num:
    total = total + i

    sum_list.append(total)


for _ in range(m):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])