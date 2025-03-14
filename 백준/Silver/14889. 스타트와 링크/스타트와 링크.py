import sys
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

start_team = [False] * N
min_diff = float('inf')  

def calculate_diff():
    start_ability = 0
    link_ability = 0
    
    for i in range(N):
        for j in range(N):
            if start_team[i] and start_team[j]:
                start_ability += S[i][j]
            elif not start_team[i] and not start_team[j]:
                link_ability += S[i][j]
    
    return abs(start_ability - link_ability)

def backtracking(idx, count):
    global min_diff
    
    if count == N//2:
        diff = calculate_diff()
        min_diff = min(min_diff, diff)
        return
    
    if idx == N:
        return
    
    start_team[idx] = True
    backtracking(idx + 1, count + 1)
    
    start_team[idx] = False
    backtracking(idx + 1, count)

backtracking(0, 0)

print(min_diff) 