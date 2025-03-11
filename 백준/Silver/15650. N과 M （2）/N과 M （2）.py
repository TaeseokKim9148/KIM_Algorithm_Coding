def backtracking(start, depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N+1):
        result.append(i)
        backtracking(i+1, depth+1)

        result.pop()

N, M = map(int, input().split())

result = []

backtracking(1, 0) 