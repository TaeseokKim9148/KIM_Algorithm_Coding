import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

count = 0

remain = K

for i in range(N-1, -1, -1):
    coin_count = remain // coin[i]

    count += coin_count

    remain -= coin_count * coin[i]

    if remain == 0:
        break

print(count)