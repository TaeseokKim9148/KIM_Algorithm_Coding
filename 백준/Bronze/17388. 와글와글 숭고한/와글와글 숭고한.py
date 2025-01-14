s, k, h = map(int, input().split())
u = {s : 'Soongsil', k : 'Korea', h: 'Hanyang'}
if s + k + h >= 100:
    print('OK')
else:
    print(u[min(s, k, h)])