moves = []
for _ in range(36):
    moves.append(input())

visited = [[False] * 6 for _ in range(6)]

x = ord(moves[0][0]) - ord('A')
y = int(moves[0][1]) - 1
visited[x][y] = True

for i in range(35):
    x1 = ord(moves[i][0]) - ord('A')
    y1 = int(moves[i][1]) - 1
    
    x2 = ord(moves[i+1][0]) - ord('A')
    y2 = int(moves[i+1][1]) - 1

    if visited[x2][y2]:
        print("Invalid")
        exit()
        
    if abs(x1-x2) * abs(y1-y2) != 2:
        print("Invalid")
        exit()
        
    visited[x2][y2] = True

x1 = ord(moves[-1][0]) - ord('A')
y1 = int(moves[-1][1]) - 1
x2 = ord(moves[0][0]) - ord('A')
y2 = int(moves[0][1]) - 1

if abs(x1-x2) * abs(y1-y2) != 2:
    print("Invalid")
    exit()

print("Valid")  