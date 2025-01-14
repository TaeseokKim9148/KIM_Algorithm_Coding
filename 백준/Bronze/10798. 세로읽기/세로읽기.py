words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]): # 각 열에서 현재 인덱스 j가 해당 문자열의 길이보다 작은지 확인
            print(words[i][j], end='')