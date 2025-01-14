N = int(input())
a = 0
for _ in range(N):
    A, B = map(int, input().split())
    a += B % A
print(a)

# 사과 개수를 학생수로 나눈 나머지를 더해준다. 