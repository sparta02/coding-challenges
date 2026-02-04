N = int(input())
B = [int(input()) for _ in range(N)]

# 1 (2) (3) 4 (5) 6

# 그리디 알고리즘
# 1. 만약 A가 B를 이길 수 있다면, B 카드 보다 큰 카드 중 가장 작은 카드를 낸다
# 2. 만약 A가 B를 이길 수 없다면, 가장 작은 카드를 낸다

A = [ x for x in range(1, 2*N+1) if x not in B]

# 최종 점수
result=0

# B보다 큰 숫자들 중 가장 작은 index 반환
def search_index(target):
    left=0
    right=len(A)-1
    mid_idx=9999999

    while left<=right:
        mid= (left+right)//2
        if A[mid]>target:
            mid_idx=min(mid_idx, mid)
            right=mid-1
        else:
            left=mid+1
    return mid_idx


for i in range(N):
    B_card = B[i]
    #print(f"B 카드: {B_card}")

    A_index=search_index(B_card)

    # Case 1. A가 이길 수 있는 경우
    if A_index != 9999999:
        A.pop(A_index)
        # print("이김")
        # print(A)
        result+=1
    # Case 2. A가 이길 수 없는 경우
    else:
        A.pop(0)
        # print("이길 수 없음")
        # print(A)
        

print(result)

