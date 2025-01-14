
T = int(input())

for _ in range(T):
    
    K = int(input())
    
    
    participants = list(map(int, input().split()))
    
    
    N = int(input())
    
    
    qualified = []
    
    for _ in range(N):
       
        participant_info = list(map(int, input().split()))
        participant_number = participant_info[0]
        hours = participant_info[1]
        minutes = participant_info[2]
        
        
        if hours == -1 and minutes == -1:
            continue
        
        
        if hours < 6 or (hours == 6 and minutes == 0):
            
            if participant_number in participants:
                total_minutes = hours * 60 + minutes
                qualified.append((participant_number, total_minutes))
    
    
    qualified_count = len(qualified)
    
    
    if qualified:
        
        best_participant = min(qualified, key=lambda x: x[1])
        best_participant_number = best_participant[0]
    else:
        best_participant_number = None
    
    
    print(best_participant_number, qualified_count)