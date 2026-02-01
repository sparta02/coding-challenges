import heapq
import sys

def solve():
    # 모든 입력을 한꺼번에 읽어서 공백 단위로 나눔
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        m = int(input_data[idx])
        idx += 1
        
        # m개의 숫자를 가져옴
        arr = input_data[idx : idx + m]
        idx += m
        
        max_heap = [] # 중앙값 이하 (최대 힙)
        min_heap = [] # 중앙값 초과 (최소 힙)
        result = []
        
        for i in range(m):
            num = int(arr[i])
            
            # 1. 두 힙의 균형을 맞추며 삽입
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            
            # 2. 왼쪽 최대값이 오른쪽 최소값보다 크면 교체
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                left_max = -heapq.heappop(max_heap)
                right_min = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -right_min)
                heapq.heappush(min_heap, left_max)
            
            # 3. 홀수 번째 원소(i=0, 2, 4...)일 때 중앙값 저장
            if i % 2 == 0:
                result.append(str(-max_heap[0]))
        
        # 한 줄에 모든 결과 출력
        print(" ".join(result))

if __name__ == "__main__":
    solve()