n = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(n)]
#print(bombs)

# n초에서 1초까지 내려가면서
# 현재 초~n초 중 가장 값이 큰 폭탄을 해체
result=0
for i in range(n, 0, -1):
    #print(f"{i}번째 시간")
    biggest_bomb=-1
    index=-1
    for j in range(len(bombs)):
        if bombs[j][1]>=i and biggest_bomb<bombs[j][0]:
            index=j
            biggest_bomb=bombs[j][0]
    #print(biggest_bomb)
    if index!=-1:
        score, time = bombs.pop(index)
        result+=score
    #print(bombs)

print(result)


# #2 1
# 10 1
# #1 2
# 10 3
# #4 4
# 8 4
# 9 5
# 10 5
# 3 7
# 2 8






