from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))
q = deque(range(1, N+1))
cnt = 0

for target in nums:                    
    pos = q.index(target)             
    left_move = pos                   
    right_move = len(q) - pos         
    
    if left_move <= right_move:       
        q.rotate(-pos)                
        cnt += left_move
    else:                             
        q.rotate(right_move)         
        cnt += right_move
    
    q.popleft()                       

print(cnt)