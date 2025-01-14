from collections import deque

def find_parents(N, edges):
    
    tree = [[] for _ in range(N + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

  
    parents = [0] * (N + 1)

   
    queue = deque([1])
    parents[1] = -1  

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if parents[neighbor] == 0: 
                parents[neighbor] = node
                queue.append(neighbor)

    return parents


N = int(input())
edges = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges.append((a, b))


parents = find_parents(N, edges)


for i in range(2, N + 1):
    print(parents[i])