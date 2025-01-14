while True:
    n = int(input())
    if n == 0:
        break

    prime = [True] * (2*n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int((2*n + 1)**0.5) +1):
        if prime[i]:
            for j in range(i *i, 2*n + 1, i):
                prime[j] = False
    count =0
    for i in range(n + 1, 2*n + 1):
        if prime[i]:
            count += 1

    print(count)