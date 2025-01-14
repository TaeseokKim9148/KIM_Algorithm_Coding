n, m = map(int, input().split())

song = []
em_yimel = []

for _ in range(n):
    s = input().split()
    song.append(s[1])
    em_yimel.append(s[2] + s[3] + s[4])

for _ in range(m):
    a, b, c = input().split()
    find = a + b + c
    answer = []

    for i in range(n):
        if em_yimel[i] == find:
            answer.append(song[i])
    

    if len(answer) == 0:
        print('!')
    elif len(answer) == 1:
        print(answer[0])

    else:
        print('?')