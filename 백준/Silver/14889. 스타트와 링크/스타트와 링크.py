def calculate_team_stat(team, stats):
    team_stat = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                team_stat += stats[team[i]][team[j]]
    return team_stat

N = int(input())
stats = []
for _ in range(N):
    stats.append(list(map(int, input().split())))

min_diff = 10000  

def check_teams(team, index):
    global min_diff
    
    if len(team) == N // 2:
        start_team = team
        link_team = [i for i in range(N) if i not in start_team]
        
        start_stat = calculate_team_stat(start_team, stats)
        link_stat = calculate_team_stat(link_team, stats)
        
        diff = start_stat - link_stat
        if diff < 0:
            diff = -diff
        
        if diff < min_diff:
            min_diff = diff
        return

    if index == N:
        return
        
    check_teams(team + [index], index + 1)

    check_teams(team, index + 1)


check_teams([], 0)


print(min_diff)