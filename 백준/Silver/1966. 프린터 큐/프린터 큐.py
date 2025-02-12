import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n, m = map(int, input().split())
    
    priorities = list(map(int, input().split()))
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    
    printed_order = 0
    
    while queue:
        current = queue.popleft()
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            printed_order += 1
            if current[1] == m:
                print(printed_order)
                break