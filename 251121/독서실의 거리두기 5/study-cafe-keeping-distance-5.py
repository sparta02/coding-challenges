N = int(input())
seat = input()

# Please write your code here.

result=seat.find("1")
#print(result)
끝=seat.count("1")
for i in range(끝+1):
    if i == 끝:
        result=max(result, len(seat))
        #print(N-1-seat.find("1"))
    else:
        차이=int((seat.find("1")+1)/2)
        result=max(result,차이)
        seat=seat[seat.find("1")+1:]
        #print(차이, seat)

    
    
print(result)