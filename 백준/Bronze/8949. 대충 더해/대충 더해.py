A, B = input().split()

answer = ''

A = A[::-1] 
B = B[::-1]  

for i in range(max(len(A), len(B))):
    if i < len(A):
        a = int(A[i])
    else:
        a = 0
        
    if i < len(B):
        b = int(B[i])
    else:
        b = 0
        
    answer = str(a + b) + answer

print(int(answer))