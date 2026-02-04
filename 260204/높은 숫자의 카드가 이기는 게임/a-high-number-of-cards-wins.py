N = int(input())
B = [int(input()) for _ in range(N)]

# 1 (2) (3) 4 (5) 6

# 그리디 알고리즘
# 1. 만약 A가 B를 이길 수 있다면, B 카드 보다 큰 카드 중 가장 작은 카드를 낸다
# 2. 만약 A가 B를 이길 수 없다면, 가장 작은 카드를 낸다

A = [ x for x in range(1, 2*N+1) if x not in B]

# 최종 점수
result=0

for i in range(N):
    B_card = B[i]
    print(f"B 카드: {B_card}")

    # Case 2. A가 이길 수 없는 경우
    if max(A)<B_card:
        A.pop(0)
        #print("이길 수 없음")
        #print(A)
    # Case 1. A가 이길 수 있는 경우
    else:
        for A_card in A:
            if A_card>B_card:
                A.remove(A_card)
                break
        #print("이김")
        #print(A)
        result+=1

print(result)

