n = int(input())  
pi = list(map(int, input().split()))  

a = 0  # 최대 증가량을 저장할 변수
b = 0  # 현재 증가량을 저장할 변수

for i in range(1, n):
    if pi[i] > pi[i - 1]:  
        b += pi[i] - pi[i - 1]  
    else:  
        a = max(a, b)
        b = 0  


c = max(a, b)

print(c)