n = int(input())
m = int(input())

car = m
m_car = m

for _ in range(n):
    icar, ocar = map(int, input().split())
    car += icar - ocar
    if car < 0 :
        print(0)
        exit()
    
    if car > m_car:
        m_car = car

        
print(m_car)  