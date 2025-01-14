alpha = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
broken = list(map(int, input().split()))
message = input()

last_number = 0

for ch in message:
    for idx, alpha_list in enumerate(alpha):
        if ch in alpha_list:
            push_number = broken.index(idx) + 1
            
            if push_number == last_number:
                print('#', end='')
            for _ in range(alpha_list.index(ch) + 1):
                print(push_number, end='')
                
            last_number = push_number
            break