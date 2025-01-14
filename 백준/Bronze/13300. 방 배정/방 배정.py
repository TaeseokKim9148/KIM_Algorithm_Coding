n, k = map(int, input().split())


select_room = [[0] * 7 for _ in range(2)]  


for _ in range(n):
    S, Y = map(int, input().split())
    select_room[S][Y] += 1  


room_number = 0
for S in range(2):
    for Y in range(1, 7): 
        student_number = select_room[S][Y]
        room_number += (student_number + k - 1) // k  


print(room_number)