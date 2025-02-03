k = int(input())  

n = 9999999

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체 
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

count = 0
for i in range(n + 1):
    if is_prime[i]:
        count += 1
        if count == k:
            print(i)
            break  