n, m = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.
arr=[]

for pair in pairs:
    pair.sort()
    arr.append(pair)

result=0 # 최종적으로 출력할 결과
for item in arr: 
    temp_count= arr.count(item)
    result=max(result, temp_count)

print(result)