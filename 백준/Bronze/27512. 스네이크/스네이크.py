n, m = map(int, input().split())


if n % 2 == 0 or m % 2 == 0:
    max_long = n * m

else:
    max_long = n * m - 1

print(max_long)