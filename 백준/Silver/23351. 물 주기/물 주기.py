import sys
input = sys.stdin.readline

N, K, A, B = map(int, input().split())

moisture = [K] * N

day = 0

while True:
    day += 1
    
    min_moisture = min(moisture)
    
    best_start = 0
    best_sum = float('inf')
    
    for i in range(N - A + 1):
        current_sum = sum(moisture[i:i+A])
        if current_sum < best_sum:
            best_sum = current_sum
            best_start = i
    
    for i in range(best_start, best_start + A):
        moisture[i] += B
    
    for i in range(N):
        moisture[i] -= 1
    
    if moisture[i] == 0:
        print(day)
        exit()