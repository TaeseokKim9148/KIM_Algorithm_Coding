N = int(input())
string = input()

if len(string) != N:
    print("NO!")
    exit()

rainbow_lower = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
rainbow_upper = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

can_make_lower = True
can_make_upper = True

for char in rainbow_lower:
    if char not in string:
        can_make_lower = False
        break

for char in rainbow_upper:
    if char not in string:
        can_make_upper = False
        break

if can_make_lower and can_make_upper:
    print("YeS")
elif can_make_lower:
    print("yes")
elif can_make_upper:
    print("YES")
else:
    print("NO!")