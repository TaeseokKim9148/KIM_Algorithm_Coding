n, m, k = map(int, input().split())


f, d = map(int, input().split())
min_distance = (m - d + 1) + (f - 1) 
winner = 1  


for i in range(2, k + 1):
    f, d = map(int, input().split())
    distance = (m - d + 1) + (f - 1)

    if distance < min_distance:
        min_distance = distance
        winner = i
    elif distance == min_distance:
        winner = min(winner, i)

print(winner)