while True:
    day, month, year = map(int, input().split())
    
    if day == 0 and month == 0 and year == 0:
        break
        
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29    
    

    total_days = day
    for i in range(month - 1):  
        total_days += days_in_month[i]
    
    print(total_days)