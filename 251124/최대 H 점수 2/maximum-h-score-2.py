from itertools import combinations

N, L = map(int, input().split())
arr = list(map(int, input().split()))

def h_index(a):
    a.sort(reverse=True)
    h = 0
    for i in range(len(a)):
        if a[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

# L이 0이면 바로 H-index 계산
if L == 0:
    print(h_index(arr[:]))
    exit()

result = 0

# 0개부터 L개까지 선택해서 모두 탐색
for k in range(0, L + 1):
    for comb in combinations(range(N), k):
        temp = arr[:]
        for idx in comb:
            temp[idx] += 1
        
        result = max(result, h_index(temp))

print(result)
