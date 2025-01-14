n = int(input())  

X, Y = 0, 0  


c_l = [input() for _ in range(n)]

for c in c_l:
    if c == 'D':  
        X += 1
    elif c == 'P':  
        Y += 1


    if 2 <= max(X, Y) - min(X,Y):
        break

print(f'{X}:{Y}')