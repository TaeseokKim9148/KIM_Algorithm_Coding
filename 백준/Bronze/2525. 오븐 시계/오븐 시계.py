A, B = map(int,input().split())
C = int(input())

total_m = A * 60 + B + C

end_hour = (total_m // 60) % 24
end_minute = total_m % 60

print(end_hour, end_minute)