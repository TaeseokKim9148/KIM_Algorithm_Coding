N, W, H, L = map(int, input().split())
a = W // L
b = H // L

print(min(a * b, N))