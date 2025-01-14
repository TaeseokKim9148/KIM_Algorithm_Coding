t = int(input())


for _ in range(t):
    
    n = int(input())
    
    
    escaped_students = 0
    for i in range(1, n+1):
        if i * i <= n:
            escaped_students += 1
        else:
            break
    
    print(escaped_students)