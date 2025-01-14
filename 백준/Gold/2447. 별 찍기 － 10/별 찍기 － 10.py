def draw_stars(n):
    # 기본 패턴 정의 (기본 단위 패턴)
    if n == 1:
        return ['*']
    
    # 크기 n//3 패턴 얻기
    smaller_pattern = draw_stars(n // 3)
    
    # 현재 크기의 패턴 리스트 생성
    pattern = []
    
    for i in range(3):
        for line in smaller_pattern:
            if i == 1:  # 중앙에 공백을 둬야 할 경우
                pattern.append(line + ' ' * (n // 3) + line)
            else:
                pattern.append(line * 3)
    
    return pattern

# 입력 받기
n = int(input())

# 패턴 생성 및 출력
result = draw_stars(n)
for line in result:
    print(line)
