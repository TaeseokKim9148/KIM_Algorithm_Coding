R, C = map(int, input().split())

parking = []
for _ in range(R):
    parking.append(input())

answer = [0, 0, 0, 0, 0]

for i in range(R-1):
    for j in range(C-1):
        if '#' in (parking[i][j], parking[i][j+1], 
                  parking[i+1][j], parking[i+1][j+1]):
            continue
            
        cars = 0
        if parking[i][j] == 'X': cars += 1
        if parking[i][j+1] == 'X': cars += 1
        if parking[i+1][j] == 'X': cars += 1
        if parking[i+1][j+1] == 'X': cars += 1
        
        answer[cars] += 1

for count in answer:
    print(count)