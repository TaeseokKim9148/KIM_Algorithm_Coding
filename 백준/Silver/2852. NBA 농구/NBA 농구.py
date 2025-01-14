N = int(input())  

score1 = score2 = 0  
team1_time = team2_time = 0  
last_time = 0 

for _ in range(N):
    team, time = input().split()
    team = int(team)
    min, sec = map(int, time.split(':'))
    current_time = min * 60 + sec  
    
    if score1 > score2:
        team1_time += current_time - last_time
    elif score2 > score1: 
        team2_time += current_time - last_time
    
   
    if team == 1:
        score1 += 1
    else:
        score2 += 1
        
    last_time = current_time

if score1 > score2:
    team1_time += 48 * 60 - last_time
elif score2 > score1:
    team2_time += 48 * 60 - last_time

print(f"{team1_time // 60:02d}:{team1_time % 60:02d}")
print(f"{team2_time // 60:02d}:{team2_time % 60:02d}")