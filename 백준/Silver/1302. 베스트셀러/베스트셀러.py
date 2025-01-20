n = int(input())  
titles = []  

for _ in range(n):
    titles.append(input())

titles.sort()

max_count = 1  
current_count = 1  
best_book = titles[0]  

for i in range(1, n):
    if titles[i] == titles[i-1]:
        current_count += 1
    else:
        current_count = 1


    if current_count > max_count:
        max_count = current_count
        best_book = titles[i]

print(best_book)  