arr=["apple", "banana", "grape", "blueberry", "orange"]

a = input()
cnt=0

for x in arr:
    if x[2]==a or x[3]==a:
        cnt+=1
        print(x)

print(cnt)