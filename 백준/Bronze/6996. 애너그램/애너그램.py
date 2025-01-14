T = int(input())  

for case in range(1, T + 1):
    
    word1, word2 = input().split()
    
    
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    if sorted_word1 == sorted_word2:
        print(f"{word1} & {word2} are anagrams.")
    else:
        print(f"{word1} & {word2} are NOT anagrams.")