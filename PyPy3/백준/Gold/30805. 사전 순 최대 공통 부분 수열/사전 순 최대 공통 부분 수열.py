n=int(input())
A= list(map(int, input().split()))
m=int(input())
B= list(map(int, input().split()))


def sol(arr1, arr2, result=[]):
    if (not arr1) or (not arr2):
        return result
    
    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2= arr1.index(tmp1), arr2.index(tmp2)

    if tmp1==tmp2:
        result.append(tmp1)
        return sol(arr1[idx1+1:], arr2[idx2+1:],result)
    elif tmp1>tmp2:
        arr1.pop(idx1)
        return sol(arr1, arr2, result)
    else:
        arr2.pop(idx2)
        return sol(arr1, arr2, result)

ans=sol(A,B)

# print(ans)
print(len(ans))

if ans:
    print(*ans)