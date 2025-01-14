R, C = map(int, input().split())


card = []


for i in range(R):
    line = list(input())
    card.append(line + line[::-1])


for i in range(R -1, -1, -1):
    card.append(card[i][::-1])

a, b = map(int, input().split())    

if card[a-1][b-1] == '#':
    card[a-1][b-1] = '.'
else:
    card[a-1][b-1] = '#'

for row in card:
    print(''.join(row))