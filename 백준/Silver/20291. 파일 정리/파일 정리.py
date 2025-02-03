n = int(input())

ext_counts = {}

for _ in range(n):
    file_name = input().strip()          
    parts = file_name.split('.')        
    ext = parts[-1]                      
   
    if ext in ext_counts:
        ext_counts[ext] = ext_counts[ext] + 1
    else:
        ext_counts[ext] = 1
# 딕셔너리의 키(확장자)들을 사전순으로 정렬
sorted_ext = sorted(ext_counts.keys())

for ext in sorted_ext:
    print(ext, ext_counts[ext])    