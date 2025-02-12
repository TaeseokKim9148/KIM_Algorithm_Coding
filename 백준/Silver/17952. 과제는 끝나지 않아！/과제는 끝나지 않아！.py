import sys
input = sys.stdin.readline

n = int(input().strip())
total_score = 0
st = []

for _ in range(n):
    data = input().split()
    if data[0] == '1':
        st.append([int(data[1]), int(data[2])])

    if st:
        st[-1][1] -=1

        if st[-1][1] == 0:
            total_score += st[-1][0]
            st.pop()


print(total_score)    