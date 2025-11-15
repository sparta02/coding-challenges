n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [ 0 for _ in range(300)]
for seg in segments:
    for i in range(seg[0]+100, seg[1]+100):
        arr[i]+=1

print(max(arr))
