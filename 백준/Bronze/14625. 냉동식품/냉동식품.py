start_h, start_m = map(int, input().split())
end_h, end_m = map(int, input().split())
N = int(input())


count = 0


current_h = start_h
current_m = start_m


while True:
    
    if current_h == end_h and current_m == end_m:
        
        time_str = f"{current_h:02d}{current_m:02d}"
        if str(N) in time_str:
            count += 1
        break
    
    
    time_str = f"{current_h:02d}{current_m:02d}"
    if str(N) in time_str:
        count += 1
    
    
    current_m += 1
    if current_m == 60:
        current_m = 0
        current_h += 1
        if current_h == 24:
            current_h = 0

print(count)