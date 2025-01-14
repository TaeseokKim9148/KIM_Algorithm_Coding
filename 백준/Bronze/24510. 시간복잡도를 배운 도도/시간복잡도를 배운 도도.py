c = int(input())  
total = 0  


for _ in range(c):
    line = input()
   
    count_for = line.count('for')
    count_while = line.count('while')
   
    loop = count_for + count_while
    total = max(total, loop)


print(total)