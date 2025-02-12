import sys
input = sys.stdin.readline

n = int(input().strip())
company = set()  

for _ in range(n):
    data = input().split()  
    name = data[0]          
    states = data[1]        

    if states == "enter":
        company.add(name)   
    else:
        if name in company:
            company.remove(name)  

result = sorted(company, reverse=True)
for name in result:
    print(name)    