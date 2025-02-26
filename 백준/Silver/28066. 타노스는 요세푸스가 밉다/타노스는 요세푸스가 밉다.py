import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

squirrels = deque(range(1, N+1))

while len(squirrels) > 1:
    
    first = squirrels.popleft()
    remove_count = min(K-1, len(squirrels))
    for _ in range(remove_count):
        squirrels.popleft()
    squirrels.append(first)

print(squirrels[0])