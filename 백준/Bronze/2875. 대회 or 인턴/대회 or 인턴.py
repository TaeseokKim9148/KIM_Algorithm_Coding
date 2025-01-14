N, M, K = map(int, input().split())

team = 0
while True:
    N -= 2 # 여자의 경우의 수
    M -= 1 # 남자의 경우의 수 
    # 남은 여자 혹은 남자가 0명 미만이거나, 인턴십 보낼 학생이 부족할  때
    if N < 0 or M < 0 or (N+M) < K: 
        break
    team += 1
print(team)
