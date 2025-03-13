N, M = map(int, input().split()) 
numbers = list(map(int, input().split()))  
numbers.sort()  

result = []  

def backtrack():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for num in numbers:
        result.append(num)  
        backtrack()  
        result.pop()  

backtrack()  