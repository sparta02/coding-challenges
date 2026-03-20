import heapq

t= int(input())

for _ in range(t):
    k=int(input())

    pq1=[]
    pq2=[]
    maps={}    
    cnt=0

    for _ in range(k):
        op, n = input().split()
        n=int(n)

        if op=='I':
            heapq.heappush(pq1, n)
            heapq.heappush(pq2, -n)
            maps[n]=maps.get(n,0)+1
            cnt+=1
            # print(pq1)
            # print(pq2)
            # print(maps)
        elif op=='D' and cnt>0:
            if n==1:
                while True:
                    temp=-heapq.heappop(pq2)
                    if maps.get(temp, 0)>0:
                        maps[temp]-=1
                        if maps[temp]==0:
                            maps.pop(temp)
                        break
                cnt-=1
            elif n==-1:
                while True:
                    temp=heapq.heappop(pq1)
                    if maps.get(temp, 0)>0:
                        maps[temp]-=1
                        if maps[temp]==0:
                            maps.pop(temp)
                        break
                cnt-=1
            # print(pq1)
            # print(pq2)
            # print(maps)
        # else:
        #     print('ignore')
    #     print()
    # print(pq1)
    # print(pq2)
    # print(maps)

    if cnt==0:
        print('EMPTY')
    else:
        while True:
            temp=-heapq.heappop(pq2)
            if maps.get(temp, 0)>0:
                print(temp, end=" ")
                break
        
        while True:
            temp=heapq.heappop(pq1)
            if maps.get(temp, 0)>0:
                print(temp)
                break
        
        
