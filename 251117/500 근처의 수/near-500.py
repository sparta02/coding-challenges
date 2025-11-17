arr=list(map(int, input().split()))
max=-1
min=9999
for ar in arr:
    if ar<500 and max<ar:
        max=ar
    if ar>500 and min>ar:
        min=ar

print(max, min)