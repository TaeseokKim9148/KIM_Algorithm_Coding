button = {
    'A': 1, 'B': 2, 'C': 3,
    'D': 1, 'E': 2, 'F': 3,
    'G': 1, 'H': 2, 'I': 3,
    'J': 1, 'K': 2, 'L': 3,
    'M': 1, 'N': 2, 'O': 3,
    'P': 1, 'Q': 2, 'R': 3, 'S': 4,
    'T': 1, 'U': 2, 'V': 3,
    'W': 1, 'X': 2, 'Y': 3, 'Z': 4,
    ' ': 1
}

number = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9,
    ' ': 1
}

# 입력 받기
p, w = map(int, input().split())  
text = input()  

total_time = 0  
prev_num = 0   

for char in text:

    curr_num = number[char]
    
    if prev_num == curr_num and curr_num != 1: 
        total_time += w
    
    total_time += button[char] * p
    
    prev_num = curr_num

print(total_time)  