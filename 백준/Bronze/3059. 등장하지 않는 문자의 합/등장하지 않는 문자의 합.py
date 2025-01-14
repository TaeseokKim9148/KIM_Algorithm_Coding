al = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

t = int(input())

for _ in range(t):
    a = set(input())
    b = al - a
    t_sum = sum(ord(char) for char in b) # 아스키코드 값의 합 ord: 아스키코드로 변환, char: 문자열의 개별 문자
    print(t_sum)