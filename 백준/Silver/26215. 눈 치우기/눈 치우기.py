import sys

input = sys.stdin.readline

N = int(input())

snow = list(map(int, input().split()))

max_snow = max(snow)

total_snow = sum(snow)

if max_snow <= total_snow / 2:
    if total_snow % 2 == 0:
        answer = total_snow // 2

    else:
        answer = total_snow // 2 + 1

else:
    answer = max_snow

if answer > 1440:
    print(-1)
else:
    print(answer)