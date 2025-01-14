a = []

for i in range(5):
    number = int(input())

    if number in a:
        a.remove(number)
    else:
        a.append(number)
print(a[0])