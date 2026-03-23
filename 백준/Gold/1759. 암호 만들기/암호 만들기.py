L, C = map(int, input().split())
arr=list(input().split())
arr.sort()
# print(arr)
mother=['a', 'e', 'i', 'o', 'u']

result=[]
a=0
b=0
# 현재 선택된 갯수, 최근 선택된 위치, L
def choose(num, curr, L):
    # print(num, curr, L)
    global a, b
    
    if num==L:
        if a>=1 and b>=2:
            print("".join(result))
        return
    
    if curr<C:
        if arr[curr] in mother:
            result.append(arr[curr])
            a+=1
            choose(num+1, curr+1, L)
            result.pop()
            a-=1
            choose(num, curr+1, L)
        else:
            result.append(arr[curr])
            b+=1
            choose(num+1, curr+1, L)
            result.pop()
            b-=1
            choose(num, curr+1, L)

choose(0, 0, L)