board = []
for _ in range(5):
    row = list(map(int, input().split()))
    board.append(row)

numbers = []
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        numbers.append(row[j])

check = [[0]*5 for _ in range(5)]

for count in range(25):
    present = numbers[count]  
    
    for i in range(5):
        for j in range(5):
            if board[i][j] == present:
                check[i][j] = 1
    
    bingo = 0
    
    for i in range(5):
        if sum(check[i]) == 5:
            bingo += 1
    
    for j in range(5):
        if sum(check[i][j] for i in range(5)) == 5:
            bingo += 1
    
    if sum(check[i][i] for i in range(5)) == 5:
        bingo += 1
    
    if sum(check[i][4-i] for i in range(5)) == 5:
        bingo += 1
    
    if bingo >= 3:
        print(count + 1)
        break