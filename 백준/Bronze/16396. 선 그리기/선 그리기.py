N = int(input())  
check = [0] * 10001  


for _ in range(N):
    x, y = map(int, input().split())
 
    if x > y:
        x, y = y, x

    for i in range(x, y):  
        check[i] = 1

result = sum(check)
print(result)