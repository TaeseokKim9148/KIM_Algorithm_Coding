from itertools import permutations # 주어진 리스트의 모든 순열을 생성

n, m = map(int, input().split())


numbers = list(range(1, n + 1))


for i in permutations(numbers, m):
    print(' '.join(map(str, i)))