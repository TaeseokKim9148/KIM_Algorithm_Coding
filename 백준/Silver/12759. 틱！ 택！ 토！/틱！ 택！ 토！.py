board = [[0]*3 for _ in range(3)]

current_player = int(input())

for turn in range(9):
    # 좌표 입력
    x, y = input().split()
    x = int(x) - 1  # 1을 빼서 0부터 시작하는 위치로 변경
    y = int(y) - 1
    
   
    board[x][y] = current_player
    
    
    winner = 0
    
    # 가로 확인
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            winner = board[i][0]
            break
            
    # 세로 확인
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            winner = board[0][i]
            break
    
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != 0:
        winner = board[0][2]
    
    if winner != 0:
        print(winner)
        break
    
    current_player = 2 if current_player == 1 else 1
    
    if turn == 8:
        print(0)  