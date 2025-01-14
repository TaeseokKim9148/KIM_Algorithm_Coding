n = int(input())
size = 4*n-3  


board = []
for i in range(size):
    board.append([' ']*size)


x = 0  
y = 0
temp_n = n

while temp_n > 0:
    curr_size = 4*temp_n-3
    
    
    for i in range(curr_size):
        board[x][y+i] = '*'
    
    
    for i in range(curr_size):
        board[x+i][y+curr_size-1] = '*'
    
  
    for i in range(curr_size):
        board[x+curr_size-1][y+i] = '*'
    
    
    for i in range(curr_size):
        board[x+i][y] = '*'
    
    
    x += 2
    y += 2
    temp_n -= 1

for row in board:
    print(''.join(row))