import sys
input = sys.stdin.readline

N = int(input())
total_votes = int(input())
students = list(map(int, input().split()))

frames = []

for time, student in enumerate(students):
        
    found = False
    for i in range(len(frames)):
        if frames[i][0] == student:
            frames[i][1] += 1  
            found = True
            break
    
    if not found:
        if len(frames) < N:
            frames.append([student, 1, time])
        else:
            
            min_vote = 1001  
            min_idx = 0
            
            for i in range(len(frames)):
                
                if frames[i][1] < min_vote:
                    min_vote = frames[i][1]
                    min_idx = i
                elif frames[i][1] == min_vote and frames[i][2] < frames[min_idx][2]:
                    min_idx = i
            
            frames[min_idx] = [student, 1, time]

for i in range(len(frames)):
    for j in range(len(frames)-1):
        if frames[j][0] > frames[j+1][0]:
            frames[j], frames[j+1] = frames[j+1], frames[j]

print(' '.join(str(frame[0]) for frame in frames))