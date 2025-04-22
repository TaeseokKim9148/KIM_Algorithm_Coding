import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

current_sum = 0
max_sum = numbers[0]  

for num in numbers:
    current_sum = max(num, current_sum + num)
    
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)