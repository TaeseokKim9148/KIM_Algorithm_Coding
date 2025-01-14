word1 = input()
word2 = input()

count1 = [0] * 26 # 각 알파벳 개수를 저장할 리스트 (a-z: 0-25)
count2 = [0] * 26


for i in word1:
    count1[ord(i) - ord('a')] += 1

for i in word2:
    count2[ord(i) - ord('a')] += 1

answer = 0
for i in range(26):
    answer += abs(count1[i] - count2[i]) # 절대값

print(answer)