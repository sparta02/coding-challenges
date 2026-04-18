def calc(arr1, arr2, a, d):
    temp=0
    for b in range(len(arr1[0])):
        temp+=arr1[a][b]*arr2[b][d]
    return temp

def solution(arr1, arr2):
    answer=[]
    # 1번째 행렬 i번째 행과
    # 2번째 행렬 j번째 열
    for i in range(len(arr1)):
        temp=[]
        for j in range(len(arr2[0])):
            # print(i,j)
            temp.append(calc(arr1, arr2, i, j))
            # print(calc(arr1, arr2, i, j))
        answer.append(temp)
    return answer