n, m = map(int, input().split())

result=[]
print_result=[]
# Please write your code here.
def make(num):
    if num == m:
        temp_list=list(set(result))
        #print(result)
        #print(temp_list)
        if len(temp_list)==m:
            print_result.append(tuple(sorted(result)))

        #print()
        return
    
    for i in range(1, n+1):
        result.append(i)
        make(num+1)
        result.pop()

make(0)
print_result=list(set(print_result))
print_result.sort()
#print(print_result)
for hi in print_result:
    for j in range(m):
        print(hi[j], end=" ")
    print()