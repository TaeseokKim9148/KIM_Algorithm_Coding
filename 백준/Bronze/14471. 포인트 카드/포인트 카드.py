N, M = map(int, input().split())
cards = []


for _ in range(M):
    win = int(input().split()[0])
    cards.append(win)


cards.sort(reverse=True) # 오름차순 인터넷 참고

cost = 0

for i in range(M-1):
    if cards[i] < N:
        cost += N - cards[i]

print(cost)