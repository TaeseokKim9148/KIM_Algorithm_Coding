import sys
input = sys.stdin.readline

def back_tracking(idx, temp):
    if len(temp) == M:
        if not tuple(temp) in result:
            result.add(tuple(temp))
        return
    
    for i in range(N):
        temp.append(nums[i])
        back_tracking(idx+1, temp)
        temp.pop()

N, M = map(int, input().split())
nums = [*map(int, input().split())]
nums.sort()

result = set()
back_tracking(0, [])

for r in sorted(result):
    print(*r) 