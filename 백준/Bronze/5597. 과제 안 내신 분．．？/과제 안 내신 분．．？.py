student=[i for i in range(1,31)]
for i in range(28):
    data=int(input())
    student.remove(data) # # 28명의 출석한 학생 번호를 입력받아 리스트에서 제거
print(min(student)) # 남은 학생 중 작은 번호
print(max(student)) # 남은 학생 중 큰 번호