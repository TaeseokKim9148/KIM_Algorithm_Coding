n = int(input())

seat = list(map(int, input().split()))

pc = [0] * 101  #


reject = 0

for i in seat:
    if pc[i] == 1:
        reject += 1
    else:
        pc[i] = 1

print(reject)