n = int(input())
target = [int(input()) for _ in range(n)] 
stack = []     
result = []     
current = 1     

for num in target:

    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:  
        print('NO')
        exit(0)

for op in result:
    print(op)