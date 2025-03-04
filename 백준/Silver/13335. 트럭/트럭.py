import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())  
trucks = list(map(int, input().split())) 


time = 0  
bridge = [0] * w
weight_on_bridge = 0  
truck_idx = 0  

while True:

    time += 1
    
    weight_on_bridge -= bridge[0]
    bridge = bridge[1:] + [0]
    
    if truck_idx < n:
        if weight_on_bridge + trucks[truck_idx] <= L:
            bridge[-1] = trucks[truck_idx]
            weight_on_bridge += trucks[truck_idx]
            truck_idx += 1
    
    if truck_idx >= n and weight_on_bridge == 0:
        break

print(time)