warehouse = input()
robot = warehouse.index('@')
box = warehouse.index('#')
target = warehouse.index('!')

visited_positions = []
visited_positions.append([robot, box])

moves = []
moves.append([robot, box, 0])

while moves:
    robot, box, commands = moves.pop(0)
    if box == target:
        print(commands)
        break
    
    # 왼쪽으로 이동해보기
    new_robot = robot - 1
    if 0 <= new_robot < 10:  
        if new_robot != box and [new_robot, box] not in visited_positions:
            visited_positions.append([new_robot, box])
            moves.append([new_robot, box, commands + 1])
        # 로봇이 박스를 왼쪽으로 미는 경우:
        if new_robot == box:  
            if box - 1 >= 0:  
                new_box = box - 1  
                if [new_robot, new_box] not in visited_positions:  
                    visited_positions.append([new_robot, new_box])
                    moves.append([new_robot, new_box, commands + 1])
    
    # 오른쪽으로 이동해보기
    new_robot = robot + 1
    if 0 <= new_robot < 10:  
        if new_robot != box and [new_robot, box] not in visited_positions:
            visited_positions.append([new_robot, box])
            moves.append([new_robot, box, commands + 1])
        # 로봇이 박스를 오른쪽으로 미는 경우:
        if new_robot == box:  
            if box + 1 < 10: 
                new_box = box + 1  
                if [new_robot, new_box] not in visited_positions: 
                    visited_positions.append([new_robot, new_box])
                    moves.append([new_robot, new_box, commands + 1])
else:
    print(-1)