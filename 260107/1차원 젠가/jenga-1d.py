n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

#print(blocks)
for i in range(e1-1, s1-2,-1):
    #print(i)
    blocks.pop(i)

# print(blocks)

for i in range(e2-1, s2-2,-1):
    #print(i)
    blocks.pop(i)

#print(blocks)

print(len(blocks))
for i in range(len(blocks)):
    print(blocks[i])