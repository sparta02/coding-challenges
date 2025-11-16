N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# N명의 개발자 K번의 악수동안만 전염
# 처음 감염자 P, 총 T줄
people = [ [0, 0] for i in range(0, N+1)]
people[P][0]=1


handshakes.sort(key=lambda x: x[0])



def 감염(i, j):
    global people
    temp_a=0
    temp_b=0
    if people[i][0]==1 and people[i][1]<K:
            temp_a=1
    if people[j][0]==1 and people[j][1]<K:
            temp_b=1
    
    if temp_a==1:
        people[j][0]=1
        people[j][1]=0
        people[i][1]+=1
    if temp_b==1:
        people[i][0]=1
        people[i][1]=0
        people[j][1]+=1

for hand in handshakes:
    감염(hand[1], hand[2])


for i in range(1, N+1):
    print(people[i][0], end="")