import sys

input = sys.stdin.readline

N = int(input())
words_dict = {}

for _ in range(N):
    word = input().rstrip()
    length = len(word)

    if length not in words_dict:
        words_dict[length] = set()
    words_dict[length].add(word)

for length in sorted(words_dict):
    for word in sorted(words_dict[length]):
        print(word)
