import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

def calculate(a, b, op):
    if op == 0:      
        return a + b
    elif op == 1:    
        return a - b
    elif op == 2:    
        return a * b
    elif op == 3:    
        if b == 0:
            return 0
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def backtracking(idx, current_value):
    if idx == N:
        return current_value, current_value
    
    max_val = -int(1e9)
    min_val = int(1e9)
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1 
            
            next_value = calculate(current_value, A[idx], i)
            next_max, next_min = backtracking(idx + 1, next_value)
            
            max_val = max(max_val, next_max)
            min_val = min(min_val, next_min)
            
            operators[i] += 1 
    
    return max_val, min_val

max_result, min_result = backtracking(1, A[0])
print(max_result)
print(min_result) 