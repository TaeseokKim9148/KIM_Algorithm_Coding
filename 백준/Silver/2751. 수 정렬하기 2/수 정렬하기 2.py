import sys

n = int(sys.stdin.readline())

number = []

for _ in range(n):
    number.append(int(sys.stdin.readline()))

for i in sorted(number):
    print(i)