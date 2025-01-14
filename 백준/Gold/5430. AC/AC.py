from collections import deque

def play_game(commands, number_count, numbers):
    box = deque(numbers)
    is_flipped = False
    
    for cmd in commands:
        if cmd == 'R':
            is_flipped = not is_flipped
        elif cmd == 'D':
            if len(box) == 0:
                return "error"
            if is_flipped:
                box.pop()
            else:
                box.popleft()
    
    if is_flipped:
        box.reverse()
    return "[" + ",".join(map(str, box)) + "]"

test_count = int(input())

for _ in range(test_count):
    commands = input()
    number_count = int(input())
    input_str = input()
    
    if number_count == 0:
        numbers = []
    else:
        numbers = []
        number_string = input_str[1:-1]
        if number_string:
            for num in number_string.split(','):
                numbers.append(int(num))
    
    print(play_game(commands, number_count, numbers))