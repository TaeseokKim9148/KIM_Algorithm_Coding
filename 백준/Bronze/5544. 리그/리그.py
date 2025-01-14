n = int(input())

points = [0] * n  


for _ in range(n * (n - 1) // 2):
    A, B, C, D = map(int, input().split())
    if C > D:  
        points[A - 1] += 3
    elif C < D:  
        points[B - 1] += 3
    else:  
        points[A - 1] += 1
        points[B - 1] += 1


sorted_teams = list(range(n))


for i in range(n):
    for j in range(i + 1, n):
        if points[sorted_teams[i]] < points[sorted_teams[j]] or (
            points[sorted_teams[i]] == points[sorted_teams[j]] and sorted_teams[i] > sorted_teams[j]
        ):
            
            sorted_teams[i], sorted_teams[j] = sorted_teams[j], sorted_teams[i]


rank = [0] * n
current_rank = 1


for i in range(n):
    team = sorted_teams[i]
    if i > 0 and points[team] == points[sorted_teams[i - 1]]:
        rank[team] = current_rank  
    else:
        current_rank = i + 1  
        rank[team] = current_rank


for r in rank:
    print(r)
