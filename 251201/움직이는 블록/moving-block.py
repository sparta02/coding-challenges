n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
average_blocks= int(sum(blocks)/len(blocks))
# print(average_blocks)

# 최종 결과값
result=0
for i in range(n):
    if blocks[i]>average_blocks:
        result+=blocks[i]-average_blocks

print(result)