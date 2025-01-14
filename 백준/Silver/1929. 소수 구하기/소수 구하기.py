M, N = map(int, input().split())


prime = [True] * (N + 1)
prime[0] = prime[1] = False

for i in range(2, int(N ** 0.5) + 1):    # # N의 제곱근을 구함 인터넷 찾아봄
    if prime[i]:                          
        for j in range(i * i, N + 1, i):  
            prime[j] = False

for i in range(M, N + 1):
    if prime[i]:
        print(i)