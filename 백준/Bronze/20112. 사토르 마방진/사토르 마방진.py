n = int(input())  
words = [input().strip() for _ in range(n)]  


is_sator = True  


for i in range(n):
    for j in range(n):
        if words[i][j] != words[j][i]:  
            is_sator = False  
            break  
    if not is_sator:  
        break 

if is_sator:
    print("YES")
else:
    print("NO")