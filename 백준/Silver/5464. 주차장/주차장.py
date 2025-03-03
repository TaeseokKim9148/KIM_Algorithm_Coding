import sys
input = sys.stdin.readline

N, M = map(int, input().split())

fee_per_unit = []
for i in range(N):
    fee = int(input())
    fee_per_unit.append(fee)

car_weights = []
for i in range(M):
    weight = int(input())
    car_weights.append(weight)

parking_spaces = [0] * N

waiting_cars = []

total_income = 0

for i in range(2*M):
    car = int(input())
    
    if car > 0:
        empty_space = -1
        for j in range(N):
            if parking_spaces[j] == 0:
                empty_space = j
                break
        
        if empty_space != -1:
            parking_spaces[empty_space] = car
        else:
            waiting_cars.append(car)
    
    else:
        car = -car  
        
        for j in range(N):
            if parking_spaces[j] == car:
                fee = car_weights[car-1] * fee_per_unit[j]
                total_income += fee
                
                parking_spaces[j] = 0
                
                if waiting_cars:
                    next_car = waiting_cars.pop(0)
                    parking_spaces[j] = next_car
                
                break

print(total_income)