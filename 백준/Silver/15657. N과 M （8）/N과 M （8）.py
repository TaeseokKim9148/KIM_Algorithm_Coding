N, M = map(int, input().split()) 
numbers = list(map(int, input().split()))  
numbers.sort()  

result = []  

def backtrack(start_idx):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if i < start_idx:
            continue
        result.append(numbers[i])  
        backtrack(i)  
        result.pop()  

backtrack(0)  