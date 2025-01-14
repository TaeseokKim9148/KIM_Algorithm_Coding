N = int(input())  
scores = []
for _ in range(N):
    country, student, score = map(int, input().split())
    scores.append([score, country, student])

scores.sort(reverse=True)  

medals = []  
country_count = {}  

medal_number = 0
for score, country, student in scores:
    if medal_number >= 3:  
        break
        
    medal_count = 0
    if country in country_count:
        medal_count = country_count[country]
        
    if medal_count < 2:
        winner = [country, student]
        medals.append(winner)
        country_count[country] = medal_count + 1
        medal_number += 1

for country, student in medals:
    print(country, student)