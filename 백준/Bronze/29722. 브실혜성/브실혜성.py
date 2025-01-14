year, month, day = map(int, input().split('-'))
n = int(input())

total_days = (year - 1) * 360 + (month - 1) * 30 + (day - 1) + n

# 새로운 날짜 계산
year = total_days // 360 + 1
total_days %= 360
month = total_days // 30 + 1
day = total_days % 30 + 1

# 출력
print(f'{year:04d}-{month:02d}-{day:02d}')