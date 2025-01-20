n = int(input())  
unique_words = []  

for _ in range(n):
    word = input()
    cycle = False
    
    for unique in unique_words:
        if len(word) == len(unique):

            for i in range(len(word)):
                rotated = word[i:] + word[:i] # 문자열 슬라이싱을 이용해서 문자열 순환
                if rotated == unique:
                    cycle = True
                    break
        if cycle:
            break
    

    if not cycle:
        unique_words.append(word)

print(len(unique_words))  