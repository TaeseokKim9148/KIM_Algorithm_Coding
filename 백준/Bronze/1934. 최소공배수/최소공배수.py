import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().split())
    
    min_number = min(a, b)
    gcd = 1
    for i in range(min_number, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    
    lcm = (a * b) // gcd
    print(lcm)