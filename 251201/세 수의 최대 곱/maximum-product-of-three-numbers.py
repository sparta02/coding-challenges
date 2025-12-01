n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()
arr_minus=[ item for item in arr if item<0 ]
arr_plus=[ item for item in arr if item>0 ]
# print(arr_minus)
# print(arr_plus)
result= -999999999999999999999999999999
# Case1: 양수 3개
# 1, 2, 3, 4
if len(arr_plus)>=3:
    result=max(result, arr_plus[-1]*arr_plus[-2]*arr_plus[-3])
# Case2: 양수 2개, 음수 1개
# -2, -1, 3, 4
if len(arr_plus)>=2 and len(arr_minus)>=1:
    result=max(result, arr_plus[-1]*arr_plus[-2]*arr_minus[-1])

# Case3: 양수 1개, 음수 2개
# -3, -2, -1, 5
if len(arr_plus)>=1 and len(arr_minus)>=2:
    result=max(result, arr_plus[-1]*arr_minus[0]*arr_minus[1])


# Case4: 음수 3개
# -4, -3, -2, -1
if len(arr_minus)>=3:
    result=max(result, arr_minus[-1]*arr_minus[-2]*arr_minus[-3])

# 모두 0과 비교
if 0 in arr:
    result=max(result,0)

print(result)