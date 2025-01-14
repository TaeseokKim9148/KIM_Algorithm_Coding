n, x = map(int, input().split())  
p = list(map(int, input().split()))  

total_peple = sum(p)

if total_peple % x == 0:
    print(1)
else:
    print(0)