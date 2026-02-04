import heapq

N = int(input())
x, y = zip(*[tuple(map(int, input().split())) for _ in range(N)])
x, y = list(x), list(y)
# x는 개수, y는 값
min_heap=y[:]
heapq.heapify(min_heap)
max_heap=[ -num for num in y]
heapq.heapify(max_heap)

result=0

maps={}
for i in range(N):
    maps[y[i]]=x[i]

left=heapq.heappop(min_heap)
left_count=maps[left]
right=-heapq.heappop(max_heap)
right_count=maps[right]
life=int(sum(x)/2)

while life:
    # print(f"현재 life:{life}")
    # print(f"left: {left}, {left_count}개")
    # print(f"right: {right}, {right_count}개")
    # 작은 수가 더 많은 경우
    if left_count>right_count:
        result=max(left+right, result)
        life-=right_count
        left_count-=right_count
        if life<1:
            break
        right=-heapq.heappop(max_heap)
        right_count=maps[right]
    # 큰 수가 더 많은 경우
    elif left_count<right_count:
        result=max(left+right, result)
        life-=left_count
        right_count-=left_count
        if life<1:
            break
        left=heapq.heappop(min_heap)
        left_count=maps[left]
    # 똑같은 경우
    else:
        result=max(left+right, result)
        life-=left_count
        if life<1:
            break
        left=heapq.heappop(min_heap)
        right=-heapq.heappop(max_heap)

        left_count=maps[left]
        right_count=maps[right]
    # print(f"left: {left}, {left_count}개")
    # print(f"right: {right}, {right_count}개")

print(result)