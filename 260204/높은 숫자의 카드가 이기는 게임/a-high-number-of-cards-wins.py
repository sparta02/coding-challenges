import heapq

N = int(input())
B = [int(input()) for _ in range(N)]
heapq.heapify(B)
# 1 (2) (3) 4 (5) 6

A=[]
for x in range(1, 2*N+1):
    if x not in B:
        A.append(x)

result=0

# B를 우선순위 큐로 만든 후,
# A의 원소들을 하나씩 B의 최솟값과 비교한다
# 만일 A의 원소가 더 크다면 +1 후 B의 최솟값 pop
# 아니라면 다시 원소를 B에 넣는다

for A_card in A:
    B_min = heapq.heappop(B)
    #print(A_card)
    if A_card>B_min:
        result+=1
    else:
        heapq.heappush(B, B_min)
    # print(result)
    # print(B)

print(result)