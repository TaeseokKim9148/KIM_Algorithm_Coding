import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []

for _ in range(p):
    data = input().split()      
    level = int(data[0])       
    name = data[1]             
    entered = False            


    for room in rooms:
        if len(room["players"]) < m and room["min_level"] <= level <= room["max_level"]:
            room["players"].append((level, name))
            entered = True
            break  
    

    if not entered:
        new_room = {
            "min_level": level - 10, 
            "max_level": level + 10,  
            "players": [(level, name)]  
        }
        rooms.append(new_room)

for room in rooms:
  
    if len(room["players"]) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    sorted_players = sorted(room["players"], key=lambda x: x[1])

    for lvl, nick in sorted_players:
        print(lvl, nick) 