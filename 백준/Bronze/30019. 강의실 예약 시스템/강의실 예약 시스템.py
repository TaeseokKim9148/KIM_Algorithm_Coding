import sys

n,m = map(int, sys.stdin.readline().split())

room = [0] * n

for i in range(m):

    k,s,e = map(int, sys.stdin.readline().split())
    
    if room[k -1] <= s:
        room[k -1] = e
        print('YES')
    else:
        print('NO')