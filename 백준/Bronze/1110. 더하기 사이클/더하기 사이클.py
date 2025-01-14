n= int(input())  
ori = n  
count = 0  

while True:
    ten = n // 10  # N의 10의 자리
    one = n % 10   # N의 1의 자리
    new_num = (one * 10) + ((ten + one) % 10)  # 새로운 숫자 생성
    count += 1  
    if new_num == ori:  
        break
    n = new_num  

print(count)  