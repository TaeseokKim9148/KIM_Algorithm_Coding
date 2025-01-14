d = ['N', 'E', 'S', 'W']

state = 0

for i in range(10):
    c = int(input())
    if c == 1:
        state += 1
    elif c == 2:
        state += 2
    elif c == 3:
        state -= 1
    
   
    state %= 4


final_d = d[state]
print(final_d)