nums = []

for i in range(10):
  n = int(input())%42
  if n not in nums:
    nums.append(n) # 요소를 추가할때 쓰는 함수 

print(len(nums))

# 친구 도움을 받음

# len 함수