n, m = map(int, input().split())
arr = list(map(int, input().split()))


# 사람:     1 1 0 1 1 1
# 와이파이: 1 '1' 1 1 '1' 1
# 배열을 탐색하며 와이파이가 설치되지 않았다면
# 2m+1칸 채우기

count=0
wifi=[0]*n

for i in range(n):
    # 사람이 살고 있으나 해당 위치에 wifi가 깔려있지 않은 경우
    if arr[i]==1 and wifi[i]==0:
        count+=1
        for j in range(i, min(i+2*m+1, n)):
            wifi[j]=1
        #print(wifi)

print(count)