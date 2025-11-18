n = int(input())
arr = [int(input()) for _ in range(n)]
# Please write your code here.

def carry(a, b, c):
    a=str(a)
    b=str(b)
    c=str(c)
    max_len = max(len(a), len(b), len(c))
    
    a=a.rjust(max_len,"0")
    b=b.rjust(max_len,"0")
    c=c.rjust(max_len,"0")

    for i in range(max_len):
        #print(max_len)
        #print(int(a[i]),int(b[i]),int(c[i]))
        if int(a[i])+int(b[i])+int(c[i])>=10:
            return True
    return False

max_num=-1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            #print(arr[i],arr[j],arr[k], carry(arr[i],arr[j],arr[k]))
            if max_num<arr[i]+arr[j]+arr[k] and carry(arr[i],arr[j],arr[k])==False:
                max_num=arr[i]+arr[j]+arr[k]
            #print(max_num)

print(max_num)