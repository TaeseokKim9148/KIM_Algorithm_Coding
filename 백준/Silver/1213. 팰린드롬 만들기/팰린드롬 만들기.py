name = input()

count = {}
for i in name:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

mid = ""
odd = 0

left = ""
for x in sorted(count):
   
    if count[x] % 2 == 1:
        mid = x
        odd = odd + 1
    
    left = left + (x * (count[x] // 2))

if odd > 1:
    print("I'm Sorry Hansoo")
else:
 
    answer = left + mid + left[::-1]
    print(answer)