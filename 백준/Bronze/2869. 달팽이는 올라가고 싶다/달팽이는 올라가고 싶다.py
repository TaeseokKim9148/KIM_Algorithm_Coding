A, B, V = map(int, input().split())

days = (V - A) / (A - B)
if days == int(days):
    days = int(days)
else:
    days = int(days) + 1

print(days + 1)