import sys

T = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
total = [0] * 90001
acc = 0

for i in range(1, 90001):
    if i % 3 == 0 or i % 7 == 0:
        acc += i
    
    total[i] = acc

for i in numbers:
    print(total[i])