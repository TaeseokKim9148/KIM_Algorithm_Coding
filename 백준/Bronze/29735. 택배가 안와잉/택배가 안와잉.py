start, end = input().split()
N, T = map(int, input().split())

startH, startM = map(int, start.split(':'))
endH, endM = map(int, end.split(':'))

tot = (endH - startH) * 60 + (endM - startM)

day = (tot - 1) // T

print(N // day)

arrival_M = startM + ((N % day + 1) * T)
arrival_H = startH + (arrival_M // 60)
arrival_M = arrival_M % 60
if arrival_H >= 24:
    arrival_H = arrival_H % 24

print(f"{arrival_H:02d}:{arrival_M:02d}")  