t = int(input())  
numbers = list(map(int, input().split()))  


for n in numbers:
    
    a = 0
    for i in range(1, n):  
        if n % i == 0:
            a += i

    
    if a == n:
        print("Perfect")
    elif a < n:
        print("Deficient")
    else:
        print("Abundant")