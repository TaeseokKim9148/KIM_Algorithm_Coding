# 에라토스테네스의 체 이용
def get_prime_numbers(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
                
    return is_prime

max_num = 1000000
prime_check = get_prime_numbers(max_num)

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    for i in range(2, n//2 + 1):
        if prime_check[i] and prime_check[n-i]:
            count += 1
    
    print(count)