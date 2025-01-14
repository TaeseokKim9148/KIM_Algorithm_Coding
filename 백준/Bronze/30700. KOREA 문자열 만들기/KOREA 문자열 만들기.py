S = input()
len = 0  
order = 0   # (0: 'K', 1: 'O', 2: 'R', 3: 'E', 4: 'A')

for char in S:
    if char == 'KOREA'[order]:  
        len += 1  
        order = (order + 1) % 5  

print(len)