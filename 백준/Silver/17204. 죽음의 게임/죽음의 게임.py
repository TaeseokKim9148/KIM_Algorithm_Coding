import sys

N, K = map(int, sys.stdin.readline().strip().split())  

targets = []
for i in range(N):
    target = int(sys.stdin.readline().strip())
    targets.append(target)

visited = set()
current = 0  
path = [0]  

while True:
    next_person = targets[current]
    
    if next_person == K:
        print(len(path))
        break
    
    if next_person in visited:
        cycle_start = path.index(next_person) # 사이클 시작 위치
        cycle = path[cycle_start:]
        
        if K in [targets[p] for p in cycle]: 
            for i, p in enumerate(cycle):
                if targets[p] == K:
                    M = cycle_start + i + 1
                    print(M)
                    break
            break
        else:
            print(-1)
            break
    
    visited.add(current)
    current = next_person
    path.append(current)
    
    if len(path) > N * 2: #  경로의 길이가 사람 수(N)의 2배를 초과하는지 확인
        print(-1)
        break     