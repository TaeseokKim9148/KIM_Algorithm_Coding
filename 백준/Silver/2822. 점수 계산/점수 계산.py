scores = []
for i in range(8):
    score = int(input())
    scores.append([score, i+1])

scores.sort()  

total = 0
answer = []

for i in range(3, 8): # 가장 높은 점수 5개의 합
    total += scores[i][0] 
    answer.append(scores[i][1])  


print(total)
answer.sort()  
for x in answer:  
    print(x, end=' ')