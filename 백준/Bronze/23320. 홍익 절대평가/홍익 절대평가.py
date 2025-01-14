n = int(input())  

a = list(map(int, input().split()))  

x, y = map(int, input().split()) 


a_relative_evaluation = n * (x // 10) // 10

total = 0

for i in a:
    if i >= y:
        total += 1

a_absolute_evaluation = total  

print(a_relative_evaluation, a_absolute_evaluation)
