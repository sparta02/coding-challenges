N = int(input())
seat = input()

# Please write your code here.
arr=[]
result=seat.find("1")
#print(result)
끝에서2번째인덱스=0
for i in range(seat.count("1")-2):
    #print(seat.find("1", seat.find("1", i-1)+1), seat.find("1", seat.find("1", i)+1))
    result=max(result, int((seat.find("1", seat.find("1", i)+1)-seat.find("1", seat.find("1", i-1)+1))/2))
    끝에서2번째인덱스=seat.find("1", seat.find("1", i)+1)
    #print(int((seat.find("1", seat.find("1", i-1)+1)-seat.find("1", seat.find("1", i)+1))/2), result)
result=max(result, len(seat)-seat.find("1", 끝에서2번째인덱스+1)-1)
print(result)