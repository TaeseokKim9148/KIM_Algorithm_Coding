def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:  
            return False
    return True


def is_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        
        sum_of_squares = 0
        while n > 0:
            digit = n % 10  
            sum_of_squares += digit * digit  
            n //= 10  
        
        n = sum_of_squares
    
    return n == 1

P = int(input())

for _ in range(P):
    case_num, M = map(int, input().split())
    
    if is_prime(M) and is_happy(M):
        result = "YES"
    else:
        result = "NO"
    
    print(case_num, M, result)