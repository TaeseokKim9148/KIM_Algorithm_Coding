N = int(input()) 
moves = input()   

board = [['.'] * N for _ in range(N)]

x, y = 0, 0


for move in moves:
    nx, ny = x, y
    
    if move == 'U': nx -= 1    
    elif move == 'D': nx += 1  
    elif move == 'L': ny -= 1  
    elif move == 'R': ny += 1  
    
   
    if 0 <= nx < N and 0 <= ny < N:
        
        if move in 'UD':
            
            if board[x][y] == '.':
                board[x][y] = '|'
            
            elif board[x][y] == '-':
                board [x][y] = '+'
                
            
            if board[nx][ny] == '.':
                board[nx][ny] = '|'
            
            elif board[nx][ny] == '-':
                board [nx][ny] = '+'
        
        else:
            
            if board[x][y] == '.':
                board[x][y] = '-'
            
            elif board[x][y] == '|':
                board [x][y] = '+'
                
            
            if board[nx][ny] == '.':
                board[nx][ny] = '-'
           
            elif board[nx][ny] == '|':
                board [nx][ny] = '+'
                
        
        x, y = nx, ny

for row in board:
    print(''.join(row))