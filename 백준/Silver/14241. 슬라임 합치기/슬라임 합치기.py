N = int(input())
slime = list(map(int,input().split()))
total_score = 0

while len(slime) > 1:
    slime.sort()

    first = slime[0]
    second = slime[1]


    slime.pop(0)
    slime.pop(0)

    score = first * second
    total_score += score

    n_slime = first + second
    slime.append(n_slime)

print(total_score)