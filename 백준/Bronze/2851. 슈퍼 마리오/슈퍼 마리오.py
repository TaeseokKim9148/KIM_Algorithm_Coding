sum = 0
before = 0

for i in range(10):
    score = int(input())
    before = sum
    sum += score
    
    if sum > 100:
        gap1 = sum - 100
        gap2 = 100 - before
        
        if gap1 > gap2:
            sum = before
        break

print(sum)