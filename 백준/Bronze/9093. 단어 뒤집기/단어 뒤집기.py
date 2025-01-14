import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    sentence = input().strip()
    for word in sentence.split():
        print(word[::-1], end=' ')
    print()
