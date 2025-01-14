T = int(input()) 

for i in range(T):
    m = int(input())  
    words = [input() for _ in range(m)]  
    
    n = int(input())  
    
    if i > 0:  
        print()
    print(f'Scenario #{i + 1}:')
    
    for _ in range(n):
        password_list = list(map(int, input().split()))  
        k = password_list[0]  
        
        
        password = ''
        for idx in range(1, k + 1):
            word_idx = password_list[idx]  
            password += words[word_idx]
        print(password)