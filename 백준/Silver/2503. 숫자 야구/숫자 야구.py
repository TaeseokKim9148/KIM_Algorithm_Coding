import sys

input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    data = input().split()
    idea = data[0]
    st = int(data[1])
    bo = int(data[2])
    q.append((idea, st, bo))

count = 0

for num in range(111, 1000):
    candidate = str(num)

    if "0" in candidate:
        continue
    if len(set(candidate)) != 3:
        continue

    ok = True

    for idea, st, bo in q:
        st1 = 0
        bo1 = 0

        for i in range(3):
            if candidate[i] == idea[i]:
                st1 += 1
            elif idea[i] in candidate:
                bo1 += 1

        if st1 != st or bo1 != bo:
            ok = False
            break
    if ok:
        count += 1
        # print(candidate)
print(count)