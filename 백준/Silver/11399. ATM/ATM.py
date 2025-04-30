import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int, input().split()))

times.sort()

total_waiting_time = 0
current_waiting_time = 0

for time in times:
    current_waiting_time += time
    total_waiting_time += current_waiting_time

print(total_waiting_time)