t = int(input())  
games = []

for _ in range(t):
    games.append(input())  

for game in games:
    jjagsu_chars = ''  
    holosu_chars = ''  

    for i in range(len(game)):
        if i % 2 == 0:  # 짝수 인덱스일 때
            jjagsu_chars += game[i]
        else:  
            holosu_chars += game[i]

    if len(game) % 2 == 0:  # 문자열 길이가 짝수일 때
        print(jjagsu_chars)  
        print(holosu_chars)  
    else:  # 문자열 길이가 홀수일 때
        print(jjagsu_chars + holosu_chars)  
        print(holosu_chars + jjagsu_chars)  
