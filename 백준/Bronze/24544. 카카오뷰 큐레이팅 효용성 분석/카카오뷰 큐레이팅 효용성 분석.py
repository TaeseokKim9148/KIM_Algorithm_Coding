n = int(input())  
a = list(map(int, input().split()))  
b = list(map(int, input().split()))  


total_interest = 0
for i in range(n):
    total_interest += a[i]


not__interest = 0
for i in range(n):
    if b[i] == 0:  
        not__interest += a[i]


print(total_interest)
print(not__interest)