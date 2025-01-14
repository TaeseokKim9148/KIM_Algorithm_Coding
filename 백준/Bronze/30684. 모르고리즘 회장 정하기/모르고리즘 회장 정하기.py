n = int(input())  
candidate = ''  

for _ in range(n):
    name = input().strip()  

   
    if len(name) == 3:
       
        if candidate is '' or name < candidate:
            candidate = name

print(candidate)