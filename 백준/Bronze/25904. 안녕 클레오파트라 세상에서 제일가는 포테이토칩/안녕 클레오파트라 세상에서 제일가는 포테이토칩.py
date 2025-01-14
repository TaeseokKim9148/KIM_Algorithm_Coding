n, x = map(int, input().split())
t = list(map(int, input().split()))

voice = x  
for i in range(101):  
    person = i % n  
    
    if voice > t[person]:  
        print(person + 1)  
        break
    
    voice += 1  