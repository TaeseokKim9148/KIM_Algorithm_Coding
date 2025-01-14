y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# 만나이
if m2 > m1 or (m2 == m1 and d2 >= d1):
    print(y2-y1)
# 생일안지난 만나이
else:
    print(y2-y1-1)

# 세는나이
print(y2-y1+1)

# 연나이
print(y2-y1)