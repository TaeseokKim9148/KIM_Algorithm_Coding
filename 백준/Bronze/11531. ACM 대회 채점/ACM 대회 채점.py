problems = {}
correct = 0
penalty = 0

while True:
    line = input()
    
    if line == '-1':
        for problem in problems:
            if problems[problem][0] == 'right':
                correct += 1
                penalty += problems[problem][1]
        break

    a, b, c = line.split()
    
    if c == 'right':
        if b not in problems:
            problems[b] = ['right', int(a)]
        elif problems[b][0] == 'wrong':
            problems[b][0] = 'right'
            problems[b][1] += int(a)
    else:
        if b not in problems:
            problems[b] = ['wrong', 20]
        else:
            problems[b][1] += 20

print(correct, penalty)

