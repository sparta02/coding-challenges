def solution(str1, str2):
    answer = 0
    maps_A={}
    maps_B={}
    for i in range(len(str1)-1):
        if str(str1[i:i+2]).isalpha():
            temp=str(str1[i:i+2]).upper()
            maps_A[temp]=maps_A.get(temp, 0)+1
    for i in range(len(str2)-1):
        if str(str2[i:i+2]).isalpha():
            temp=str(str2[i:i+2]).upper()
            maps_B[temp]=maps_B.get(temp, 0)+1
            
    # print(maps_A)
    # print(maps_B)
    
    min_maps={}
    max_maps=maps_B
    for key, value in maps_A.items():
        if key in maps_B:
            min_maps[key]=min(value, maps_B[key])
        max_maps[key]=max(max_maps.get(key, 0), value)

    # print(min_maps)
    # print(max_maps)
    min_len=sum([value for _, value in min_maps.items()])
    max_len=sum([value for _, value in max_maps.items()])
    if min_len==0 and max_len==0:
        return 65536
    
    return int(min_len/max_len*65536)