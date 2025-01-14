n, k = map(int, input().split())

max_value = 0


for i in range(1, k + 1):
    result = n * i  
    gegulo_result = int(str(result)[::-1])  # str() 함수는 이 정수를 문자열로 변환
    
    
    if gegulo_result > max_value:
        max_value = gegulo_result

print(max_value)