n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

selected=[]
result=0


def check():
    global result
    a,b,c=selected
    if a&b or b&c or a&c:
        return
    else:
        result=max(result, a+b+c)

def choose(num, curr):
    if len(selected)==3:
        check()
        return

    for i in range(curr, n):
        selected.append(arr[i])
        choose(num, i+1)
        selected.pop()

choose(3,0)
print(result)