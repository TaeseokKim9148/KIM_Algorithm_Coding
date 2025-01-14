clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]


n = int(input())  


max_scores = []


for i in range(9):  
    scores = list(map(int, input().split()))
    max_scores.append(max(scores))  

max_index = max_scores.index(max(max_scores))

print(clubs[max_index])