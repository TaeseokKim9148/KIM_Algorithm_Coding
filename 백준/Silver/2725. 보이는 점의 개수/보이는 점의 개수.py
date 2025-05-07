import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

result = [0] * 1001

result[1] = 3

for i in range(2, 1001):
    count = 0
    for j in range(1, i+1):
        if i == j:
            continue
        if gcd(i, j) == 1:
            count += 2
            result[i] = result[i -1] + count

T = int(input())

for _ in range(T):
    N = int(input())
    print(result[N])