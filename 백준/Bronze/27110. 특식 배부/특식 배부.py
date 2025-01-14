N = int(input())
chicken = list(map(int, input().split()))
result = 0

# 후라이드 치킨 간장 치킨 양념치킨 
for i in range(3) :
    if chicken[i] <= N :
        result += chicken[i]
    else :
        result += N

print(result)