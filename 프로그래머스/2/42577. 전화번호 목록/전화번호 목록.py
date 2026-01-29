def solution(phone_book):
    answer = True
    phone_book= sorted(phone_book, key= lambda x: -len(x))
    #print(phone_book)
    maps={}
    for phone_num in phone_book:
        if phone_num in maps:
            return False
        for i in range(1, len(phone_num)):
            maps[phone_num[:i]]=1
        #print(maps)
        
    return True